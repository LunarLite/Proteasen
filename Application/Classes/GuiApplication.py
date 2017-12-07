import tkinter as tk
from tkinter import ttk
import csv
import sys

LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

class Gui_Application(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		self.sequence = ""
		self.algorithm = ""


		# tk.Tk.iconbitmap(self, default="clienticon.ico")
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
		label = ttk.Label(self, text="Sequence:", font=LARGE_FONT)
		label.pack(pady=10)
		self.entry = ttk.Entry(self, width = 100)
		self.entry.pack()

		
		check_frame = tk.Frame(self)
		check_frame.pack()

		self.checkbuttons = {}

		var1 = tk.IntVar()
		var1.set(0)
		checkbutton1 = ttk.Checkbutton(check_frame, text="Random", 
			variable = var1, command=lambda: self.check("Random"))
		checkbutton1.grid(row = 0, column = 0)
		self.checkbuttons["Random"] = {"button": checkbutton1, "var": var1}

		var2 = tk.IntVar()
		var2.set(0)
		checkbutton2 = ttk.Checkbutton(check_frame, text="Breadth-first", 
			variable = var2, command=lambda: self.check("Breadth-first"))
		checkbutton2.grid(row = 0, column = 1)
		self.checkbuttons["Breadth-first"] = {"button": checkbutton2, "var": var2}

		var3 = tk.IntVar()
		var3.set(0)
		checkbutton3 = ttk.Checkbutton(check_frame, text="Breadth-first with heuristic", 
			variable = var3, command=lambda: self.check("Breadth_heuristic"))
		checkbutton3.grid(row = 0, column = 2)
		self.checkbuttons["Breadth_heuristic"] = {"button": checkbutton3, "var": var3}

		var4 = tk.IntVar()
		var4.set(0)
		checkbutton4 = ttk.Checkbutton(check_frame, text="Hillclimber", 
			variable = var4, command=lambda: self.check("Hillclimber"))
		checkbutton4.grid(row = 0, column = 3)
		self.checkbuttons["Hillclimber"] = {"button": checkbutton4, "var": var4}


		# create fold button to continue
		button2 = ttk.Button(self, text="Fold", command=lambda: self.validate())
		button2.pack(pady=10, padx=10)

		# create status bar
		self.status = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=SMALL_FONT)
		self.status.pack(side = tk.BOTTOM, fill = tk.X)
	
	def run(self, csv_file):
		sequences = self.load_sequences_from_csv(csv_file)
		self.load_listbox(sequences)
		self.mainloop()

		if self.sequence == "" or self.algorithm == "":
			return sys.exit()

	def load_sequences_from_csv(self, csv_file): 
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
		self.listbox.delete(0)
		for i in range(0, len(sequences)): 
			self.listbox.insert(i, sequences[i])


	def select_from_listbox(self, event):

		a = self.listbox.curselection()
		for i in a: 
			self.entry.delete(0, tk.END)
			self.entry.insert(0, self.listbox.get(i))

	def check(self, checked):

		if(self.checkbuttons[checked]["var"].get()):
			
			for i in self.checkbuttons: 
				if i == checked:
					self.checkbuttons[checked]["button"].config(state=tk.DISABLED)
				else: 
					self.checkbuttons[i]["button"].config(state=tk.NORMAL)
					self.checkbuttons[i]["var"].set(0)

	def validate(self):

		# ensure sequence is given and only contain H and P
		if self.get("sequence") == "":
			self.status["text"] = "Warning: enter sequence"
			return False

		for c in self.get("sequence"):
			if (c.upper() != 'H' and c.upper() != 'P'):
				self.status["text"] = "Warning: sequence must contain only H and P"
				return False

		# ensure algorithm is given
		if self.get("algorithm") == None: 
			self.status["text"] = "Warning: choose algorithm"
			return False

		else: 
			self.sequence = self.get("sequence")
			self.algorithm = self.get("algorithm")					
			self.quit()
			self.withdraw()


	def get(self, g):

		if g == "algorithm": 
			for i in self.checkbuttons:
				if self.checkbuttons[i]["var"].get() == 1:
					return i

		elif g == "sequence":
			return self.entry.get()


