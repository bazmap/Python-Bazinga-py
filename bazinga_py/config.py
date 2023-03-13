# -*-coding:Utf-8 -*

# Définition des paramètres du programme
# La structure doit rester identique, seules les valeurs des variables change
# Le but est ici décraser des valeurs prédéfinies dans certains variables et d'en ajouter d'autres au besoin

# Modules requis
import os
import datetime

from bazinga_py.core.config_default import app_var



# Software
app_var['software']['name'] = "Mon programme"
app_var['software']['version'] = "1.0"
app_var['software']['resume'] = "Programme de test du framework Bazinga PY"
app_var['software']['author'] = "Arthur Bazin"
app_var['software']['copyright'] = datetime.datetime.now().strftime("%Y") + " - www.arthurbazin.com"
#app_var['software']['dir'] = ""
#app_var['config_dir']['config_dir'] = os.path.join(app_var['software']['dir'], 'config')
#app_var['config_dir']['config_file_default'] = 'default.conf'
#app_var['software']['logo'] = ""
#app_var['software']['icon'] = ""
#app_var['software']['splash_screen'] = ""



# Logs
#app_var['log']['dir'] = os.path.join(app_var['software']['dir'], 'logs'),
#app_var['log']['name'] = 'Log' + "_" + app_var['execution_date'].strftime("%Y-%m-%d_%H-%M-%S") + ".log",
#app_var['log']['prefix_to_delete'] = 'Log',
#app_var['log']['type'] = 'simple',
#app_var['log']['nb_to_keep'] = 3,
#app_var['log']['min_level'] = 'DEBUG',
#app_var['log']['stdout_levels'] = ['DEBUG']



# Initialisation des variables de configuration et d'arguments
app_var['param']['config_framework'] = {
	'ma_variable': {
		'input_scope' : ['argument','config'],
		'type' : 'string',
		'value' : 'Valeur initiale',
		'value_user' : None,
		'expected': 'Un texte au hasard',
		'group': 'Groupe 1',
		'label': 'Cette variable fait cela',
		'help' : 'Variable de démonstration numéro 1.'
	},
	'ma_variable_2': {
		'input_scope' : ['argument','config'],
		'type' : 'integer',
		'value' : 14,
		'expected': 'Un nombre entier',
		'group': 'Groupe 2',
		'label': 'Cette variable fait ceci',
		'help' : "Variable de démonstration numéro 2."
	}
}



#######################
# Variables spécifiques
#######################

# Formats spatiaux
app_var['var']['variable1'] = 'Une petite démo'


