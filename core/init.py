# -*-coding:Utf-8 -*

# Programme principal

# Modules requis
from bazinga_py.init import *

import core.tk_rootInterface as tk_rootInterface



# Initialisation de l'interface graphique
rootWindows = ba_rootWindows()



# Ajout des widgets à l'interface principale
app = tk_rootInterface.rootInterface(rootWindows)
app.pack(
	fill="both", 
	expand=True,
	padx=0,
	pady=0
)



# Bouton 1
app.Button_1.bind(
	'<ButtonPress-1>', 
	lambda event: ba_app_var['param']['init_tk']['ma_variable']['value'].set('Bouton 1')
)



# Bouton 2
app.Button_2.bind(
	'<ButtonPress-1>', 
	lambda event: ba_app_var['param']['init_tk']['ma_variable']['value'].set('Bouton 2')
)



# Bouton 3
app.Button_3.bind(
	'<ButtonPress-1>', 
	lambda event: ba_app_var['param']['init_tk']['ma_variable']['value'].set(ba_app_var['param']['init']['ma_variable']['value'])
)



# Mise en place de la boucle d'écoute d'évènement
rootWindows.run_mainloop()