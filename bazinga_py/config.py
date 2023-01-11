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
app_var['software']['author'] = "John Doe"
app_var['software']['copyright'] = datetime.datetime.now().strftime("%Y") + " - Big Society Inc"
#app_var['software']['dir'] = ""
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



# Config
#app_var['config_file']['dir'] = os.path.join(app_var['software']['dir'], 'config')
#app_var['config_file']['default_file'] = 'default.conf'



# Librairies annexes
#app_var['libraries']['dir'] = os.path.join(app_var['software']['dir'], 'lib')



# Binaires annexes
#app_var['binaries']['dir'] = os.path.join(app_var['software']['dir'], 'bin')



# Initialisation des variables de configuration et d'arguments
app_var['config']['specific'] = {
	'ma_variable': {
		'input_scope' : ['argument','config'],
		'type' : 'string',
		'default' : 'Valeur par défaut',
		'expected': 'Un texte au hasard',
		'group': 'Groupe 1',
		'help' : "Variable de démonstration."
	},
	'ma_variable_2': {
		'input_scope' : ['argument','config'],
		'type' : 'string',
		'default' : 'Valeur par défaut',
		'expected': 'Un texte au hasard',
		'group': 'Général',
		'help' : "Variable de démonstration."
	},
}



#######################
# Variables spécifiques
#######################

# Variable de démonstration
app_var['specific']['ma_varaible_2'] = "Variable de démonstration."


