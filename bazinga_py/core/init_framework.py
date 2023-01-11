# -*-coding:Utf-8 -*

# Initialisation du framework
# Le contenu ne doit pas changer

# Modules requis
import os

from bazinga_py.core import config_default
from bazinga_py import config as config_user
from bazinga_py.core import functions
from bazinga_py.core import argument_parser
from bazinga_py.core import config_file_parser
from bazinga_py.core import logger as my_logger



# Récupération des variables de configuration du programme
app_var = {**config_default.app_var, **config_user.app_var}

# Récupération des variables de configuration
app_var['config']['default'] = {**app_var['config']['framework'], **app_var['config']['specific']}

# Définition d'un gorupe par défaut
for key in app_var['config']['default']:

	if app_var['config']['default'][key]['group'] == '':
		app_var['config']['default'][key]['group'] = 'Général'



# Initialisation des arguments
var_args = argument_parser.argumentParser(
	app_var['software'], 
	app_var['config']['default']
)



# Gestion des actions à mener directement à partir des arguments
if var_args['printConfigFile'] :
	# Affichage d'un fichier de configuration par défaut
	print(functions.retrieveConfigFile(app_var['config']['default']))
	exit()

if var_args['surpriseMe'] :
	# Elément de surprise
	print(functions.surpriseMe())
	exit()



# Initialisation des fichiers de configuration
var_configParse = config_file_parser.configLoader(
	os.path.join(
		app_var['config_file']['dir'],
		functions.coalesce(var_args['configFile'], app_var['config_file']['default_file'])
	)
)



# Création des variables de configuration par défaut
app_var['config']['init'] = functions.getConfigVar(app_var['config']['default'], var_configParse[0], var_args)


# Initialisation du logger
logger = my_logger.createLogger(
	app_var['log']['name'], 
	app_var['log']['dir'], 
	app_var['log']['min_level'], 
	app_var['log']['stdout_levels'], 
	int(app_var['config']['init']['logFileNumber']['value']),  
	app_var['log']['prefix_to_delete'], 
	app_var['log']['type']
)

logger.info(app_var['software']['name'] + ' - v' + app_var['software']['version'])
logger.info(app_var['software']['author'] + ' - ' + app_var['software']['copyright'])
logger.info('')