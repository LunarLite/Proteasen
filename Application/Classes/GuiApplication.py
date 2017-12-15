# GuiApplication.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the Gui_Application class.
# Usage: 
# loading sequences to listbox: 
# > object.run("id", data)
# without loading sequences to listbox: 
# > object.run 
#
# to ask application for selected algorithm and sequence: object.get("algorithm" / "sequence")
# Note: only after continuing by clicking the fold button



import tkinter as tk
from tkinter import ttk
import csv
import sys

LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

class Gui_Application(tk.Tk):
	"""Application to select amino acid and algorithm"""

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		self.valid = False

		tk.Tk.wm_title(self, "Protein Po(w)der")
		tk.Tk.resizable(self, width = tk.FALSE, height = tk.FALSE)

		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight =1)
		
		list_frame = tk.Frame(self)
		list_frame.pack(side=tk.TOP, fill = tk.X)
		
		# create listbox and scrollbar
		self.scrollbar = tk.Scrollbar(list_frame)
		self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

		self.listbox = tk.Listbox(list_frame, selectmode = tk.EXTENDED, 
			width = 100, relief = tk.GROOVE)
		self.listbox.pack(fill = tk.X)
		self.listbox.insert(0, "No sequences available") 
		
		# connect scrollbar to listbox
		self.listbox.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.listbox.yview)

		# create select button
		button1 = ttk.Button(self, text=">> Select <<")
		button1.bind("<Button-1>", self.select_from_listbox)
		button1.pack(fill = tk.X)

		# create sequence entry bar 
		label1 = ttk.Label(self, text="Sequence:", font=LARGE_FONT)
		label1.pack(pady=10)
		self.entry1 = ttk.Entry(self, width = 100)
		self.entry1.pack()

		# create frame to set grid for checkbuttons
		check_frame = tk.Frame(self)
		check_frame.pack()

		self.checkbuttons = {}

		# create checkbuttons
		var1 = tk.IntVar()
		var1.set(0)
		checkbutton1 = ttk.Checkbutton(check_frame, text="Random", 
			variable = var1, command=lambda: self.on_checkbutton_click("Random"))
		checkbutton1.grid(row = 0, column = 0)
		self.checkbuttons["Random"] = {"button": checkbutton1, "var": var1}

		var2 = tk.IntVar()
		var2.set(0)
		checkbutton2 = ttk.Checkbutton(check_frame, text="Breadth-first", 
			variable = var2, command=lambda: self.on_checkbutton_click("Breadth"))
		checkbutton2.grid(row = 0, column = 1)
		self.checkbuttons["Breadth"] = {"button": checkbutton2, "var": var2}

		var3 = tk.IntVar()
		var3.set(0)
		checkbutton3 = ttk.Checkbutton(check_frame, text="Depth-first", 
			variable = var3, command=lambda: self.on_checkbutton_click("Depth"))
		checkbutton3.grid(row = 0, column = 2)
		self.checkbuttons["Depth"] = {"button": checkbutton3, "var": var3}

		var4 = tk.IntVar()
		var4.set(0)
		checkbutton4 = ttk.Checkbutton(check_frame, text="Hillclimber", 
			variable = var4, command=lambda: self.on_checkbutton_click("Hillclimber"))
		checkbutton4.grid(row = 0, column = 3)
		self.checkbuttons["Hillclimber"] = {"button": checkbutton4, "var": var4}

		# dimension

		# checkbuttons to determine dimension
		self.checkbuttons_dimension = {}

		var2D = tk.IntVar()
		var2D.set(0)
		checkbutton2D = ttk.Checkbutton(check_frame, text="2D", 
			variable = var2D, command=lambda: self.check("2d", self.checkbuttons_dimension))
		checkbutton2D.grid(row = 1, column = 1, sticky = "e")

		self.checkbuttons_dimension["2d"] = {"button": checkbutton2D, "var": var2D}

		var3D = tk.IntVar()
		var3D.set(0)
		checkbutton3D = ttk.Checkbutton(check_frame, text="3D", 
			variable = var3D, command=lambda: self.check("3d", self.checkbuttons_dimension))
		checkbutton3D.grid(row = 1, column = 2, sticky = "w")

		self.checkbuttons_dimension["3d"] = {"button": checkbutton3D, "var": var3D}
 

		# properties

		# create frame to set grid for checkbuttons
		property_frame = tk.Frame(self)
		property_frame.pack(pady=10)

		
		self.checkbuttons_annealing = {}

		# checkboxes to determine whether to run with simulatedannealing
		self.label6 = ttk.Label(property_frame, text="Simulated annealing:", font=SMALL_FONT)

		var11 = tk.IntVar()
		var11.set(0)
		self.checkbutton11 = ttk.Checkbutton(property_frame, text="yes", 
			variable = var11, command=lambda: self.check("Simulatedannealing", self.checkbuttons_annealing))
		self.startchain_visibility = "hidden"

		self.checkbuttons_annealing["Simulatedannealing"] = {"button": self.checkbutton11, "var": var11}

		var12 = tk.IntVar()
		var12.set(0)
		self.checkbutton12 = ttk.Checkbutton(property_frame, text="no", 
			variable = var12, command=lambda: self.check("no_Simulatedannealing", self.checkbuttons_annealing))
		self.startchain_visibility = "hidden"

		self.checkbuttons_annealing["no_Simulatedannealing"] = {"button": self.checkbutton12, "var": var12}


		self.checkbuttons_property = {}

		# checkboxes to determine wheter to start with straigth or random folded chain
		self.label2 = ttk.Label(property_frame, text="Start with:", font=SMALL_FONT)
		
		var5 = tk.IntVar()
		var5.set(0)
		self.checkbutton5 = ttk.Checkbutton(property_frame, text="random folded chain", 
			variable = var5, command=lambda: self.check("Randomhillclimber", self.checkbuttons_property))

		self.checkbuttons_property["Randomhillclimber"] = {"button": self.checkbutton5, "var": var5}

		var6 = tk.IntVar()
		var6.set(0)
		self.checkbutton6 = ttk.Checkbutton(property_frame, text="straight chain", 
			variable = var6, command=lambda: self.check("Hillclimber", self.checkbuttons_property))
		self.startchain_visibility = "hidden"

		self.checkbuttons_property["Hillclimber"] = {"button": self.checkbutton6, "var": var6}

		


		# checkboxes to determine breath first pruning 
		self.label3 = ttk.Label(property_frame, text="Pruning:", font=SMALL_FONT)

		var7 = tk.IntVar()
		var7.set(0)
		self.checkbutton7 = ttk.Checkbutton(property_frame, text="yes", 
			variable = var7, command=lambda: self.check("Breadth_heur", self.checkbuttons_property))
		self.pruning_visibility = "hidden"

		self.checkbuttons_property["Breadth_heur"] = {"button": self.checkbutton7, "var": var7}

		var8 = tk.IntVar()
		var8.set(0)
		self.checkbutton8 = ttk.Checkbutton(property_frame, text="no", 
			variable = var8, command=lambda: self.check("Breadth", self.checkbuttons_property))
		self.pruning_visibility = "hidden"

		self.checkbuttons_property["Breadth"] = {"button": self.checkbutton8, "var": var8}


		# checkboxes to determine depth first hillclimber afterwards
		self.label4 = ttk.Label(property_frame, text="Hillclimber afterwards:", font=SMALL_FONT)

		var9 = tk.IntVar()
		var9.set(0)
		self.checkbutton9 = ttk.Checkbutton(property_frame, text="yes", 
			variable = var9, command=lambda: self.check("Depth_hill", self.checkbuttons_property))

		self.checkbuttons_property["Depth_hill"] = {"button": self.checkbutton9, "var": var9}

		var10 = tk.IntVar()
		var10.set(0)
		self.checkbutton10 = ttk.Checkbutton(property_frame, text="no", 
			variable = var10, command=lambda: self.check("Depth", self.checkbuttons_property))
		self.hillafter_visibility = "hidden"

		self.checkbuttons_property["Depth"] = {"button": self.checkbutton10, "var": var10}


		# entry bar to determine number of iterations
		self.label5 = ttk.Label(property_frame, text="Iterations:", font=SMALL_FONT)

		self.entry2 = ttk.Entry(property_frame, width = 10)
		self.entry2.insert(0,'500')
		self.iterations_visibility = "hidden"


		# create fold button to continue
		button2 = ttk.Button(self, text="Fold", command=lambda: self.validate())
		button2.pack(pady=10, padx=10)


		# create status bar
		self.status = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=SMALL_FONT)
		self.status.pack(side = tk.BOTTOM, fill = tk.X)
	
	def run(self, id, sequence_data):
		"""Run application and load listbox with sequences 
		from a csv file or sequences directly from an array"""

		if (id == "csv"):
			sequences = self.load_sequences_from_csv(sequence_data)
			self.load_listbox(sequences)
		elif (id == "array"):
			self.load_listbox(sequence_data)

		self.mainloop()

		# exit program when exit application
		if self.valid == False:
			return sys.exit()

	def run_without(self):
		"""Run application without loading listbox"""
		self.mainloop()

		# exit program when exit application
		if self.valid == False:
			return sys.exit()


	def load_sequences_from_csv(self, csv_file): 
		"""load sequences from csv file into array"""

		with open(csv_file, 'r') as file:
			reader = csv.reader(file)
			sequences = []
			firstline = True
			for rows in reader: 
				if firstline: 
					firstline = False 
					continue
				sequences.append(rows[1].strip())
		return sequences

	
	def load_listbox(self, sequences):
		"""add sequences from array to listbox"""

		# clear listbox
		self.listbox.delete(0)

		# load sequences
		for i in range(0, len(sequences)): 
			self.listbox.insert(i, sequences[i])


	def select_from_listbox(self, event):
		"""enter selected sequence into entry bar"""

		a = self.listbox.curselection()
		for i in a: 
			self.entry1.delete(0, tk.END)
			self.entry1.insert(0, self.listbox.get(i))

	def on_checkbutton_click(self, checked):
		if checked == "Hillclimber":
			if self.startchain_visibility == "hidden": 
				self.show_properties("startchain")

		elif self.startchain_visibility == "not hidden": 
			self.hide_properties("startchain")


		if checked == "Hillclimber" or checked == "Random":
			if self.iterations_visibility == "hidden": 
				self.show_properties("iterations")

		elif self.iterations_visibility == "not hidden": 
			self.hide_properties("iterations")

		if checked == "Breadth": 
			if self.pruning_visibility =="hidden":
				self.show_properties("pruning")
		elif self.pruning_visibility == "not hidden":
			self.hide_properties("pruning")

		if checked == "Depth": 
			if self.hillafter_visibility == "hidden":
				self.show_properties("hillafter")
		elif self.hillafter_visibility == "not hidden":
			self.hide_properties("hillafter")


		self.check(checked, self.checkbuttons)

	def check(self, checked, checkbuttons):
		"""check selected checkbutton, and uncheck previous if any"""

		if(checkbuttons[checked]["var"].get()):
			
			# disable selected checkbutton, enable and unselect other checkbuttons
			for i in checkbuttons: 
				if i == checked:
					checkbuttons[checked]["button"].config(state=tk.DISABLED)
				else: 
					checkbuttons[i]["button"].config(state=tk.NORMAL)
					checkbuttons[i]["var"].set(0)


	def show_properties(self, prop):
		
		if prop == "startchain":
			self.label6.grid(row = 0, column = 0)
			self.checkbutton11.grid(row = 0, column = 1, sticky = "w")
			self.checkbutton12.grid(row = 0, column = 2, sticky = "w")
			self.label2.grid(row = 1, column = 0, sticky = "e")
			self.checkbutton5.grid(row = 1, column = 1)
			self.checkbutton6.grid(row = 1, column = 2)
			self.startchain_visibility = "not hidden"

		if prop == "pruning": 
			self.label3.grid(row = 0, column = 0)
			self.checkbutton7.grid(row = 0, column = 1)
			self.checkbutton8.grid(row = 0, column = 2)
			self.pruning_visibility = "not hidden"

		if prop == "hillafter":
			self.label4.grid(row = 0, column = 0)
			self.checkbutton9.grid(row = 0, column = 1)
			self.checkbutton10.grid(row = 0, column = 2)
			self.hillafter_visibility = "not hidden"

		if prop == "iterations":
			self.label5.grid(row = 2, column = 0, sticky = "e")
			self.entry2.grid(row = 2, column = 1, sticky = "w")
			self.iterations_visibility = "not hidden"


	def hide_properties(self, prop): 
		
		if prop == "startchain":
			self.label6.grid_remove()
			self.checkbutton11.grid_remove()
			self.checkbutton12.grid_remove()
			self.label2.grid_remove()
			self.checkbutton5.grid_remove()
			self.checkbutton6.grid_remove()
			self.startchain_visibility = "hidden"

		if prop == "pruning": 
			self.label3.grid_remove()
			self.checkbutton7.grid_remove()
			self.checkbutton8.grid_remove()
			self.pruning_visibility = "hidden"

		if prop == "hillafter":
			self.label4.grid_remove()
			self.checkbutton9.grid_remove()
			self.checkbutton10.grid_remove()
			self.hillafter_visibility = "hidden"

		if prop == "iterations":
			self.label5.grid_remove()
			self.entry2.grid_remove()
			self.iterations_visibility = "hidden"

		# reset checkboxes
		for i in self.checkbuttons_property: 
				self.checkbuttons_property[i]["button"].config(state=tk.NORMAL)
				self.checkbuttons_property[i]["var"].set(0)

		for i in self.checkbuttons_annealing: 
				self.checkbuttons_annealing[i]["button"].config(state=tk.NORMAL)
				self.checkbuttons_annealing[i]["var"].set(0)

		# empty status bar
		self.status["text"] = ""

	def validate(self):
		"""continue and quit application 
		if appropriate sequence and algorithm are given""" 

		# ensure sequence is given and only contains H and P
		if self.get("sequence") == "":
			self.status["text"] = "Warning: enter sequence"
			return False

		for c in self.get("sequence"):
			if (c.upper() != 'H' and c.upper() != 'P' and c.upper() != 'C'):
				self.status["text"] = "Warning: sequence must contain only H and P (and C)"
				return False

		# ensure algorithm is given
		if self.get("algorithm_type") == None: 
			self.status["text"] = "Warning: choose algorithm"
			return False

		# ensure dimension is given

		print(self.get("dimension"))
		if self.get("dimension") == None: 
			self.status["text"] = "Warning: choose dimension"
			return False


		algorithm_type = self.get("algorithm_type")
		self.specifications = {}
		self.specifications["sequence"] = self.get("sequence")
		self.specifications["dimension"] = self.get("dimension")


		# ensure all needed properties are given and determine exact algorithm to execute
		if algorithm_type == "Random":
			if self.get("iterations") == "": 
				self.status["text"] = "Warning: give number of iterations"
				return False
			if not str.isdigit(self.get("iterations")): 
				self.status["text"] = "Warning: invalid number of iterations"
				return False
			else:
				self.valid = True

				self.specifications["algorithm"] = "random"
				self.specifications["iterations"] = int(self.get("iterations"))


		if algorithm_type == "Hillclimber":

			hillclimber_type = ""
			if self.get("startwith") == None: 
				self.status["text"] = "Warning: determine start chain"
				return False

			if self.get("iterations") == "": 
				self.status["text"] = "Warning: give number of iterations"
				return False

			if self.get("annealing") == None: 
				self.status["text"] = "Warning: determine whether to run simulated annealing"
				return False
			elif self.get("annealing") == "Simulatedannealing":
				if self.get("startwith") == "random chain": 
					hillclimber_type = "randomsimulatedannealing"
				if self.get("startwith") == "straight chain":
					hillclimber_type = "simulatedannealing"

			elif self.get("annealing") == "no_Simulatedannealing":
				if self.get("startwith") == "random chain": 
					hillclimber_type = "randomhillclimber"
				if self.get("startwith") == "straight chain":
					hillclimber_type = "hillclimber"

				
			
			if not str.isdigit(self.get("iterations")): 
				self.status["text"] = "Warning: invalid number of iterations"
				return False
			else:
				self.valid = True

				self.specifications["algorithm"] = hillclimber_type
				self.specifications["iterations"] = int(self.get("iterations"))


		if algorithm_type == "Breadth":
			if self.get("pruning") == None: 
				self.status["text"] = "Warning: determine whether to run with pruning"
				return False
			else:
				self.valid = True

				self.specifications["algorithm"] = self.get("pruning")


		if algorithm_type == "Depth":
			print("hillafter", self.get("hillafter"))
			if self.get("hillafter") == None: 
				self.status["text"] = "Warning: determine whether to run the hillclimber algorithm afterwards"
				return False
			else:
				self.valid = True

				self.specifications["algorithm"] = self.get("hillafter")

		# close application			
		self.quit()
		self.withdraw()


	def get(self, g):
		""""get selected algorithm and get sequence form entry bar"""

		if g == "algorithm_type": 
			for i in self.checkbuttons:
				if self.checkbuttons[i]["var"].get() == 1:
					return i

		if g == "annealing":
			if self.checkbuttons_annealing["Simulatedannealing"]["var"].get() == 1:
				return "Simulatedannealing"

			if self.checkbuttons_annealing["no_Simulatedannealing"]["var"].get() == 1:
				return "no_Simulatedannealing"

		if g == "dimension": 
			if self.checkbuttons_dimension["2d"]["var"].get() == 1:
				return "2d"

			if self.checkbuttons_dimension["3d"]["var"].get() == 1:
				return "3d"


		elif g == "hillafter":
			if self.checkbuttons_property["Depth"]["var"].get() == 1:
				return "depth"
			if self.checkbuttons_property["Depth_hill"]["var"].get() == 1:
				return "depth_hill"

		elif g == "iterations": 
				return self.entry2.get()

		

		elif g == "pruning":
			if self.checkbuttons_property["Breadth"]["var"].get() == 1:
				return "breadth"
			elif self.checkbuttons_property["Breadth_heur"]["var"].get() == 1:
				return "breadth_heur"

		elif g == "startwith":
			if self.checkbuttons_property["Hillclimber"]["var"].get() == 1:
				return "straight chain"
			elif self.checkbuttons_property["Randomhillclimber"]["var"].get() == 1:
				return "random chain"

		elif g == "sequence":
			return self.entry1.get()

	def specs(self):
		return self.specifications


