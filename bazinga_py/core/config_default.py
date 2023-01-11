# -*-coding:Utf-8 -*

# Variables standard du framework
# Le contenu ne doit pas changer

# Modules requis
import os
import datetime
import inspect



# Initialisation de la variable principale de paramètrage
app_var = dict()



# Initialisation timestamp démarrage
app_var['execution_date'] = datetime.datetime.now()



# Récupération de la stack
fileStack = []
if __name__ != '__main__':
	for frame in inspect.stack()[1:]:
		if frame.filename[0] != '<':
			fileStack.append(frame.filename)



# Framework
app_var['framework'] = dict(
	name = "bazinga_py",
	version = "1.2",
	dir = os.path.join(os.path.dirname(__file__), '..\\')
)



# Software
app_var['software'] = dict(
	name = os.path.splitext(os.path.basename(fileStack[-1]))[0],
	version = "0.0",
	resume = "",
	author = "",
	copyright = app_var['execution_date'].strftime("%Y") + "",
	dir = os.path.dirname(fileStack[-1]),
	main_file = os.path.basename(fileStack[-1]),
	logo = os.path.normpath(os.path.join(app_var['framework']['dir'], 'media\\software_icon.gif'), ),
	icon = os.path.normpath(os.path.join(app_var['framework']['dir'], 'media\\software_icon.gif'), ),
	splash_screen = os.path.normpath(os.path.join(app_var['framework']['dir'], 'media\\software_splash_screen.gif'), )
)



# Logs
app_var['log'] = dict(
	dir = os.path.join(app_var['software']['dir'], 'logs'),
	name = 'Log' + "_" + app_var['execution_date'].strftime("%Y-%m-%d_%H-%M-%S") + ".log",
	prefix_to_delete = 'Log',
	type = 'simple',
	nb_to_keep = 10,
	min_level = 'DEBUG',
	stdout_levels = ['DEBUG']
)



# Config
app_var['config_file'] = dict (
	dir = os.path.join(app_var['software']['dir'], 'config'),
	default_file = 'default.conf'
)



# Librairies annexes
app_var['libraries'] = dict (
	dir = os.path.join(app_var['software']['dir'], 'lib'),
)



# Binaires annexes
app_var['binaries'] = dict (
	dir = os.path.join(app_var['software']['dir'], 'bin'),
)



# Initialisation des variables de configuration et d'arguments
app_var['config'] = dict()

app_var['config']['framework'] = {
	'configFile': {
		'input_scope' : ['argument'],
		'type' : 'string',
		'default' : app_var['config_file']['default_file'],
		'default_user' : None,
		'expected': 'Nom d\'un fichier en ".conf"',
		'group': 'Général',
		'help' : "Nom du fichier de configuration à utiliser. Les valeurs passées en argument seront utilisées à la place de celles spécifiées dans le fichier de configuration."
	},
	'printConfigFile': {
		'input_scope' : ['argument'],
		'type' : 'boolean',
		'default' : False,
		'expected': 'True/False',
		'group': 'Général',
		'help' : "Affichage d'un fichier de configuration par défaut. Aucun traitement n'est effectué."
	},
	'logFileNumber': {
		'input_scope' : ['argument','config'],
		'type' : 'integer',
		'default' : app_var['log']['nb_to_keep'],
		'expected': 'n',
		'group': 'Log',
		'help' : "Nombre de fichier de log à conserver."
	},
	'surpriseMe': {
		'input_scope' : ['argument'],
		'type' : 'boolean',
		'default' : False,
		'expected': 'True/False',
		'group': 'Général',
		'help' : "A vous de voir."
	}
}



#######################
# Variables spécifiques
#######################

# Liste de variables spécifiques au programme
app_var['specific'] = dict()