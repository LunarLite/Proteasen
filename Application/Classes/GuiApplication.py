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
			variable = var2, command=lambda: self.on_checkbutton_click("Breadth-first"))
		checkbutton2.grid(row = 0, column = 1)
		self.checkbuttons["Breadth-first"] = {"button": checkbutton2, "var": var2}

		var3 = tk.IntVar()
		var3.set(0)
		checkbutton3 = ttk.Checkbutton(check_frame, text="Breadth-first (pruning)", 
			variable = var3, command=lambda: self.on_checkbutton_click("Breadth_heur"))
		checkbutton3.grid(row = 0, column = 2)
		self.checkbuttons["Breadth_heur"] = {"button": checkbutton3, "var": var3}

		var4 = tk.IntVar()
		var4.set(0)
		checkbutton4 = ttk.Checkbutton(check_frame, text="Hillclimber", 
			variable = var4, command=lambda: self.on_checkbutton_click("Hillclimber"))
		checkbutton4.grid(row = 0, column = 3)
		self.checkbuttons["Hillclimber"] = {"button": checkbutton4, "var": var4}

		var5 = tk.IntVar()
		var5.set(0)
		checkbutton5 = ttk.Checkbutton(check_frame, text="Hillclimber (random)", 
			variable = var5, command=lambda: self.on_checkbutton_click("Randomhillclimber"))
		checkbutton5.grid(row = 0, column = 4)
		self.checkbuttons["Randomhillclimber"] = {"button": checkbutton5, "var": var5}

		# create frame to set grid for checkbuttons
		property_frame = tk.Frame(self)
		property_frame.pack()

		self.label2 = ttk.Label(property_frame, text="Iterations:", font=SMALL_FONT)
		# self.label1.grid(row = 0, column = 0)

		self.entry2 = ttk.Entry(property_frame, width = 10)
		self.entry2.insert(tk.END, '500')
		self.iterations_visibility = "hidden"
		# self.entry2.grid(row = 0, column = 0)
		

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
		if checked == "Hillclimber" or checked == "Randomhillclimber" or checked == "Random":
			if self.iterations_visibility == "hidden": 
				self.show_properties("iterations")

		elif self.iterations_visibility == "not hidden": 
			self.hide_properties("iterations")

		self.check(checked)

	def check(self, checked):
		"""check selected checkbutton, and uncheck previous if any"""

		if(self.checkbuttons[checked]["var"].get()):
			
			# disable selected checkbutton, enable and unselect other checkbuttons
			for i in self.checkbuttons: 
				if i == checked:
					self.checkbuttons[checked]["button"].config(state=tk.DISABLED)
				else: 
					self.checkbuttons[i]["button"].config(state=tk.NORMAL)
					self.checkbuttons[i]["var"].set(0)

	def show_properties(self, prop):
		# widget.pack()
		if prop == "iterations":
			self.label2.grid(row = 0, column = 0)
			self.entry2.grid(row = 0, column = 1)
			self.iterations_visibility = "not hidden"

	def hide_properties(self, prop): 
		# widget.pack_forget()
		if prop == "iterations":
			self.label2.grid_remove()
			self.entry2.grid_remove()
			self.iterations_visibility = "hidden"

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
		if self.get("algorithm") == None: 
			self.status["text"] = "Warning: choose algorithm"
			return False

		# when iterative algorithm, ensure number of iterations is given
		if self.get("algorithm") == "Hillclimber" or self.get("algorithm") == "Randomhillclimber":
			if self.get("iterations") == "": 
				self.status["text"] = "Warning: give number of iterations"
				return False
			if not str.isdigit(self.get("iterations")): 
				self.status["text"] = "Warning: invalid number of iterations"
				return False
			else:
				self.valid = True

				# close application			
				self.quit()
				self.withdraw()

		else: 
			self.valid = True

			# close application			
			self.quit()
			self.withdraw()


	def get(self, g):
		""""get selected algorithm and get sequence form entry bar"""

		if g == "algorithm": 
			for i in self.checkbuttons:
				if self.checkbuttons[i]["var"].get() == 1:
					return i

		if g == "iterations": 
			if self.valid == False:
				return self.entry2.get()
				
			if self.valid == True: 
				return int(self.entry2.get())

		elif g == "sequence":
			return self.entry1.get()


