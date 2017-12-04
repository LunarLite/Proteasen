import tkinter as tk

class Selector_App(tk.Frame):
	def __init__(self, root = None): 
		tk.Frame.__init__(self, root)

		# set window
		self.root = root
		self.root.title("Enter Sequence")
		self.root.resizable(width = tk.FALSE, height = tk.FALSE)

		self.container = tk.Frame(self.root)
		self.container.pack(fill=tk.X, padx=10, pady=20)

		self.top_frame = tk.Frame(self.container)
		self.top_frame.pack(side=tk.TOP, pady=10)
		
		self.list_frame = tk.Frame(self.top_frame)
		self.list_frame.pack(side=tk.TOP)

		self.bottom_frame = tk.Frame(self.container)
		self.bottom_frame.pack(pady=10)

		self.sequence_frame = tk.Frame(self.bottom_frame)
		self.sequence_frame.pack(side = tk.TOP)

		self.algo_frame = tk.Frame(self.bottom_frame)
		self.algo_frame.pack(side = tk.BOTTOM)


		# default mode selected sequence

		self.chosen_sequence = ""

		# create checkboxes for algorithms
		self.algorithm = Algorithm_Selector(self.algo_frame)

		# create sequence bar 
		self.sequence = Sequence_Selector(self.list_frame, self.top_frame, self.sequence_frame)


		# create fold button to continue
		self.continue_button = tk.Button(self.algo_frame, text="Fold", bg="red", fg = "white")
		self.continue_button.bind("<Button-1>", self.get)
		self.continue_button.grid(row=1, column = 1, pady = 20, ipadx = 20, ipady = 5)


		# create status bar
		self.status = tk.Label(self.root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
		self.status.pack(side = tk.BOTTOM, fill = tk.X)

	def load_sequence_list(self, sequences_array): 
		self.sequence.init_list(sequences_array)


	def get(self, event): 
		self.selected_algorithm = algorithm.get()
		self.selected_sequence = sequence.get()

		if self.validate():
			self.chosen_sequence = self.selected_sequence
			self.chosen_algorithm = self.selected_algorithm

			self.root.quit()
			self.root.withdraw()

	def validate(self): 
		if self.selected_sequence == "":
			self.status["text"] = "Warning: enter sequence"
			return False

		if self.selected_algorithm == "": 
			self.status["text"] = "Warning: choose algorithm"
			return False

		if self.selected_algorithm == "depth":
			self.status["text"] = "Warning: depth-first is not implemented yet"
			return False

		# Ensure sequence contains only H and P
		for c in self.selected_sequence:
			if (c.upper() != 'H' and c.upper() != 'P'):
				self.status["text"] = "Warning: sequence must contain only H and P"
				return False

		else: return True




class Sequence_Selector(Selector_App): 
	def __init__(self, root, root2, root3):
		self.root = root 
		self.root2 = root2
		self.root3 = root3

		# default mode selected sequence
		self.selected_sequence = ""
		
		# create sequence entry bar 
		self.label = tk.Label(self.root3, text="Sequence:", font='Helvetica 12  bold')
		self.label.pack(pady=10)
		self.entry = tk.Entry(self.root3, width = 100)
		self.entry.pack()


	def init_list(self, sequences):
		# create window to select sequence from list

		# create listbox and scrollbar
		self.Lb = tk.Listbox(self.root, selectmode = tk.EXTENDED, width = 100, relief = tk.GROOVE)
		self.Lb.pack(fill = tk.X)

		self.scrollbar = tk.Scrollbar(self.root)
		self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

		# attach listbox to scrollbar
		self.Lb.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.Lb.yview)

		# create select button
		self.select_button = tk.Button(self.root2, text=">> Select <<", relief = tk.GROOVE)
		self.select_button.bind("<Button-1>", self.select)
		self.select_button.pack(fill = tk.X)
 
		for i in range(0, len(sequences)): 
			self.Lb.insert(i, sequences[i])

	
	def select(self, event):
		a = self.Lb.curselection()
		for i in a: 
			self.entry.delete(0, END)
			self.entry.insert(0, self.Lb.get(i))

	def get(self):
		return self.selected_sequence






class Algorithm_Selector: 
	def __init__(self, root): 
		self.root = root

		# default mode selected algorithm
		self.selected_algorithm = ""
		
		self.var1 = tk.IntVar()
		self.var1.set(0)
		self.algorithm_1 = tk.Checkbutton(self.root, text="Random", variable = self.var1, command = self.select_1)
		self.algorithm_1.grid(row = 0, column = 0)

		self.var2 = tk.IntVar()
		self.var2.set(0)
		self.algorithm_2 = tk.Checkbutton(self.root, text="Breadth-first", variable = self.var2, command = self.select_2)
		self.algorithm_2.grid(row = 0, column = 1)

		self.var3 = tk.IntVar()
		self.var3.set(0)
		self.algorithm_3 = tk.Checkbutton(self.root, text="Depth-first", variable = self.var3, command = self.select_3)
		self.algorithm_3.grid(row = 0, column = 2)


	def select_1(self):
		if(self.var1.get()):
			self.algorithm_1.config(state=DISABLED)
			self.var2.set(0)
			self.algorithm_2.config(state=NORMAL)
			self.var3.set(0)
			self.algorithm_3.config(state=NORMAL)

			self.selected_algorithm = "random"

	def select_2(self):
		if(self.var2.get()):
			self.algorithm_2.config(state=DISABLED)
			self.var1.set(0)
			self.algorithm_1.config(state=NORMAL)
			self.var3.set(0)
			self.algorithm_3.config(state=NORMAL)

			self.selected_algorithm = "breadth"

	def select_3(self): 
		if(self.var3.get()):
			self.algorithm_3.config(state=DISABLED)
			self.var1.set(0)
			self.algorithm_1.config(state=NORMAL)
			self.var2.set(0)
			self.algorithm_2.config(state=NORMAL)

			self.selected_algorithm = "depth"

	def get(self): 
		return selected_algorithm


