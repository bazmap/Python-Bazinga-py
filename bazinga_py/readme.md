# Bazinga Py

## Introduction
Bazinga Py est un framework d'assistance à la conception d'application Python.
Il ne repose que sur des modules standards évitant l'installation de composants spécifiques lors du déploiement de l'application sur d'autres systèmes.

Le principe est d'utiliser ce framework comme un module Python.
Celui-ci apporte alors les éléments suivants :
- Un sytème de gestion de fichiers de configuration
- Un système de gestion des arguments passés au programme
- Un système de gestion des logs
- Une base d'interface graphique
- Un ensemble de variables en lien avec l'application
- Un ensemble de fonctions utiles


## Utilisation
Le framework peut être placé n'importe où dans le répertoire du programme à développer.
Pour l'utiliser, il suffit de compléter le fichier config.py à la racine du répertoire du framework puis d'utiliser le fichier init.py comme tout autre module Python.

L'image de l'écran d'accueil et l'icone peuvent être configurés à votre guise dans les variables `ba_app_var['log']['icon']` et `ba_app_var['log']['splash_screen']`.


## API
Le fichier init.py donne accès aux fonctionnalités suivantes :
- `ba_app_var`
- `ba_logger`
- `ba_functions`
- `ba_tk`
- `ba_rootWindows`

### ba_app_var
`ba_app_var` est une variable de type dictionnaire stockant un ensemble d'informations sur l'application.

Parmis ces information on retrouve les clés suivantes :
- `ba_app_var['execution_date']` : timestamp de démarrage du programme
  
- `ba_app_var['framework']` : informations sur le framework
  - `ba_app_var['framework']['name']` : nom
  - `ba_app_var['framework']['version']` : version
  - `ba_app_var['framework']['dir']` : répertoire d'installation
  
- `ba_app_var['software']` : informations sur le programme
  - `ba_app_var['log']['name']` : nom
  - `ba_app_var['log']['version']` : version
  - `ba_app_var['log']['resume']` : descritpion
  - `ba_app_var['log']['author']` : auteur
  - `ba_app_var['log']['copyright']` : mention légale
  - `ba_app_var['log']['dir']` : répertoire d'installation
  - `ba_app_var['log']['main_file']` : fichier utilisé pour le lancement du programme
  - `ba_app_var['log']['logo']` : emplacement du logo de l'application (fichier gif)
  - `ba_app_var['log']['icon']` : emplacement de l'icone de l'application (fichier gif)
  - `ba_app_var['log']['splash_screen']` : emplacement de l'image de l'écran de démarrage de l'application (fichier gif).  
  Attention, la taille de l'image défini la taille de l'écran de démarrage, une taille de 640x360 est en générale assez bien adaptée.
  
- `ba_app_var['log']` : informations sur les logs
  - `ba_app_var['log']['dir']` : répertoire de stockage des logs
  - `ba_app_var['log']['name']` : nom des fichiers de log
  - `ba_app_var['log']['prefix_to_delete']` : préfixe des fichiers de log à supprimer lors de la rotation. Ce prefixe doit être présent dans `ba_app_var['log']['name']`.
  - `ba_app_var['log']['type']` : gestion des fichiers de log, les fichiers de log des executions précédentes sont automatiquement supprimé selon le paramètre `ba_app_var['log']['nb_to_keep']` :
   - `simple`: un fichier de log est créé par execution. 
   - `rotating`: plusieurs fichiers de log peuvent être créées par execution : un nouveau est automatiquement créé lorsque le premier atteind 2Mo.
  - `ba_app_var['log']['nb_to_keep']` : nombre de fichier de log à conserver.
  - `ba_app_var['log']['min_level']` : niveau minimum des message à logguer parmis :
    - `NOTSET`
    - `DEBUG`
    - `INFO`
    - `WARNING`
    - `ERROR`
    - `CRITICAL`
  - `ba_app_var['log']['stdout_levels']` : liste des niveaux de log à afficher sur la sortie standard parmis :
    - `NOTSET`
    - `DEBUG`
    - `INFO`
    - `WARNING`
    - `ERROR`
    - `CRITICAL`
  
- `ba_app_var['config_file']` : informations sur la configuration
  - `ba_app_var['config_file']['dir']` : répertoire de stockage des fichiers de configuration
  - `ba_app_var['config_file']['default_file']` : fichier par défaut
  
- `ba_app_var['libraries']` : informations sur les librairies annexes
  - `ba_app_var['libraries']['dir']` : répertoire de stockage des librairies annexes
  
- `ba_app_var['binaries']` : informations sur les binaires annexes
  - `ba_app_var['binaries']['dir']` : répertoire de stockage des binaires annexes
  
- `ba_app_var['config']` : variables utilisables dans les fichiers de configuration et dans les arguments.
  - `ba_app_var['config']['framework']` : configuration initiale des variables fournies par le framework.
  - `ba_app_var['config']['specific']` : configuration des variables spécifiques à l'application.
  - `ba_app_var['config']['default']` : synthèse des variables fournies par le framework et spécifique à l'application.
  - `ba_app_var['config']['init']` : valeurs des variables fournies par le framework et spécifique à l'application après récupération du fichier de configuration, et des arguments.  
  **C'est la variable de configuration à utiliser !**


La dernière variable `ba_app_var['config']` mérite un peu d'attention. En effet, le but est de définir un ensemble de variables modifiables par l'utilisateur via un fichier de configuration ou des arguments passés au programme.  

Plusieurs variables sont définies par le framework :
- `configFile` : nom du fichier de configuration à utiliser - defaut : `ba_app_var['config_file']['default_file']`
- `printConfigFile` : affichage d'un fichier de configuration type (dans la console).
- `logFileNumber` : nombre de fichir de log à conserver - defaut : `ba_app_var['log']['nb_to_keep']`  

L'auteur du programme peut définir autant de variables modifiable que nécessaire dans `ba_app_var['config']['specific']`  
Chaque variable modifible doit être définie avec le dictionnaire suivant :
```
app_var['config']['specific'] = {
	'ma_variable': {
		'input_scope' : ['argument','config'],
		'type' : 'boolean',
		'default' : False,
		'default_user' : None,
		'expected': 'True/False',
		'group': '',
		'help' : "Affichage des formats d'import supportés ainsi que des arguments spécifiques passés à OGR. Aucun traitement n'est effectué."
	}
} 
```

Avec :
- `ma_variable` : mot clé utilisé pour appeler la variable ainsi que dans les arguments et le fichier de configuration.
- `input_scope` : fonction pouvant configurer la variable :
  - `argument` : en argument.
  - `config`: dans le fichier de configuration.
- `type` : type de donnée de la variable parmi :
  - `string`
  - `boolean`
  - `integer`
  - `float`
- `default` : valeur par défaut de la variable.
- `default_user` : valeur par défaut de la variable présentée à l'utilsiateur lors de la génération d'un fichier de configuration type.  
Par exemple la valeur vide `''` au lieu de `None` (nul).  
Cette propriété ne doit pas être déclarée si elle n'est pas utilisée.
- `expected` : valeurs attendue et présentées comme aide à l'utilisateur.
- `group` : groupe auquel appartien la variable (utilisé dans les fichiers de configuration).
- `help` : description de la variable présentées comme aide à l'utilisateur.

Notez que toute variable fournie dans un fichier de configuration, même non listée par l'auteur du programme dans `app_var['config']['specific']` sera récupérée et associée à la variable `app_var['config']['default']`.

La variable `app_var['config']['default']` reprend toutes les varaibles de `app_var['config']['framework']` et `app_var['config']['specific']` avec leurs paramètres de configurations.

La variable `app_var['config']['init']` contient les valeurs après récupération du fichier de configuration et des arguments.  
L'ordre de récupération des valeurs est le suivant :
- 1 - Valeur par défaut
- 2 - Valeur du fichier de configuration
- 3 - Valeur de l'argument  

La valeur d'un argument écrase donc la valeur du fichier de configuration qui écrase la valeur par défaut.

Attention, les variables `ba_app_var['config']['framework']`, `ba_app_var['config']['specific']` et `ba_app_var['config']['default']` possèdent la même structure (celle défine dans le fichier config.py).  
La variable `ba_app_var['config']['init']` possède la même structure sauf pour les éventuelles variables présentes dans le fichier de configuration mais non définies par le programmeur dans le fichier config.py. Pour ces variables, seule la valeur récupérée et le groupe sont disponibles via les clés suivantes :
- `ba_app_var['config']['init'][ma_variable]['group']`
- `ba_app_var['config']['init'][ma_variable]['value']`

Lorsque la classe `ba_rootWindows()` est initialisée, des varaibles de controle Tkinter sont automatiquement initialisées en se basant sur les variables `ba_app_var['config']['init'][clé]['value']`. Plus d'information dans le paragraphe sur `ba_rootWindows()`.



### ba_logger
Il s'agit de l'interface de log qui est basée sur le module `logging` fourni en standard avec Python.  
`ba_logger` est un objet `logging.logger` avec toutes ses methodes et initialisé avec les propriétés renseignées dans la variable `ba_app_var['log']`.  

Notez que le nom du logger (`logging.getLogger(name)`) est initialisé avec la variable `ba_app_var['log']['name']` ce qui ne permet pas l'utilisation de plusieurs instance de logger en parallèle.  

Pour logguer un message il suffit d'utiliser l'une des méthodes fournie par l'objet `logging.logger` :
- `ba_logger.debug(msg)`
- `ba_logger.info(msg)`
- `ba_logger.warning(msg)`
- `ba_logger.error(msg)`
- `ba_logger.critical(msg)`
- `ba_logger.exception(msg)`
- `ba_logger.log(level, msg)`  

Notez que l'objet `ba_logger` ne donne pas accès au module `logging` et que ce dernier devra donc être appelé si vous avez besoin de ses éléments.



### ba_functions
ba_fonction fournis une série de fonctions qui peuvent êtres utiles :
- `coalesce(*args)` : le premier argument non nul est renvoyé.
- `dprint(my_dict)` : affichage d'un dictionnaire.
- `checkFontAvailability(*fontName)` : la première police passée en argument et présente dans la liste des polices disponible est retournée.  
Si aucune des polices listées n'est disponible, alors la police par défaut est retournée.
- `set_mousewheel(widget)` : lie le défilement vertical d'un widget tkinter fourni au défilement de la molette.



### ba_rootWindows
`ba_rootWindows()` est une classe héritée de `ba_tk.Tk()` et permet l'initialisation de l'interface graphique de l'application.

L'appel à cette fenêtre se fait sous la forme suivante :  
`root = ba_rootWindows()`  
Il suffit ensuite d'utiliser `root` comme d'élément de base de l'interface du programme (le mot clé `root` est libre, tout autre nom peut être utilisé)

En plus des méthodes définies pour `ba_tk.Tk()` les méthodes suivantes sont disponibles :
- `openSplashScreen()` : ouvre l'écran d'accueil, l'objet `Toplevel()` associé est instancié dans `ba_rootWindows.splashScreen`.
- `openInfoScreen()` : ouvre l'écran d'information, l'objet `Toplevel()` associé est instancié dans `ba_rootWindows.infoScreen`.
- `openHelpScreen()` : ouvre l'écran d'aide, l'objet `Toplevel()` associé est instancié dans `ba_rootWindows.helpScreen`.
- `run_mainloop()` : ferme l'écran d'accueil et lance la méthode mainloop().

Notez que l'instanciation de `ba_rootWindows()` appelle la fonction `openSplashScreen()`. L'objet `Toplevel()` associé est détruit lors de l'appel à la méthode `run_mainloop()` : une fois le programme chargé. Il est possible d'empêcher le chargement de l'écran d'accueil avec l'argument `openSplashScreen = False` passé à la classe :
`root = ba_rootWindows(openSplashScreen = False)`

A l'instantiation de `ba_rootWindows()`, des variables de contrôle tkinter sont initialisées sur la base des variables de configuration (`ba_app_var['config']['init'][clé]`). Vous retrouverez ainsi la variable `ba_rootWindows.widget_var` qui possède la même structure que la variable de configuration `ba_app_var['config']['init']` avec une différence, la clé `'value'` est une variable de contrôle tkinter instanciée au lieu d'une simple valeur. Il faudra donc utiliser les méthodes `.set()` et `.get()` pour définir et récupérer la valeur.  
Voici la structure de `ba_rootWindows.widget_var` pour une clé :
- `self.widget_var['ma_variable']['input_scope']`
- `self.widget_var['ma_variable']['type']`
- `self.widget_var['ma_variable']['default']`
- `self.widget_var['ma_variable']['expected']`
- `self.widget_var['ma_variable']['group']`
- `self.widget_var['ma_variable']['help']`
- `self.widget_var['ma_variable']['value']`


La fenêtre principale `ba_rootWindows()` possède un menu référencé sous le nom `ba_rootWindows.rootMenuBar`.
Deux sous-menus sont présents :
- `ba_rootWindows.rootMenuBar.menu_fichier`
- `ba_rootWindows.rootMenuBar.menu_aide`



### ba_tk
`ba_tk` est un module qui étant les possibilités de tkinter en redéfinissant certains objets :
- `Tk()` et `Toplevel()` - ajout des méthodes suivantes :
  - `centerScreen(element)` : centrage automatique d'une fenêtre tkinter
  - `putOnTop(element, always=False)` : affichage d'une fenêtre trkinter (`tk.Tk()` ou `tk.Toplevel()`) au premier plan.  
Always permer de spécifier si la fenêtre doit recouvrir les autres programmes et maintenir ce recouvrement.
- `Text()` - ajout de la méthode suivante :
  - `insertResize()` : redimentionne automatiquement le widget à chaque insertion d'une nouvelle ligne.
