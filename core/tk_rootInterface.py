# -*-coding:Utf-8 -*

# Interface graphique de la fenêtre principale



# Modules requis
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from bazinga_py.init import ba_app_var



# Définition d'une classe d'interface
class rootInterface(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		ttk.Frame.__init__(self, parent, *args, **kwargs)

		# Create widgets :)
		self.definition_widgets(parent)



	def definition_widgets(self, parent):

		# Cadre 1
		self.frame_1 = ttk.Frame(self)
		self.frame_1.pack(
			fill = "both", 
			expand = True,
			padx = 0,
			pady = 10
		)
		self.frame_1.rowconfigure(0, weight = 1)
		self.frame_1.rowconfigure(1, weight = 1)
		self.frame_1.columnconfigure(0, weight = 1)
		self.frame_1.columnconfigure(1, weight = 1)
		self.frame_1.columnconfigure(2, weight = 1)

		# Bouton 1
		self.Button_1 = ttk.Button(
			self.frame_1, 
			text = 'Valeur 1'
		)
		self.Button_1.grid(
			row = 0,
			column = 0
		)

		# Bouton 2
		self.Button_2 = ttk.Button(
			self.frame_1, 
			text = 'Valeur 2'
		)
		self.Button_2.grid(
			row = 0,
			column = 1
		)

		# Bouton 3
		self.Button_3 = ttk.Button(
			self.frame_1, 
			text = 'Réinitialiser'
		)
		self.Button_3.grid(
			row = 0,
			column = 2
		)

		# Label
		self.my_Label = ttk.Label(
			self.frame_1, 
			textvariable = ba_app_var['param']['init_tk']['ma_variable']['value']
		)
		self.my_Label.grid(
			row = 1,
			column = 1
		)
