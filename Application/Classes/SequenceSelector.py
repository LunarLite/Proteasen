from tkinter import *

class Sequence_Selector:
	def __init__(self, master): 

		# set window
		self.root = master
		self.root.title("Enter Sequence")

		self.container = Frame(self.root)
		self.container.pack(fill=X, padx=10, pady=20)

		self.top_frame = Frame(self.container)
		self.top_frame.pack(side=TOP, pady=10)
		
		self.list_frame = Frame(self.top_frame)
		self.list_frame.pack(side=TOP)

		self.bottom_frame = Frame(self.container)
		self.bottom_frame.pack(pady=10)

		self.sequence_frame = Frame(self.bottom_frame)
		self.sequence_frame.pack(side = TOP)

		self.algo_frame = Frame(self.bottom_frame)
		self.algo_frame.pack(side = BOTTOM)


		# default mode selected sequence
		self.selected_sequence = ""
		self.selected_algorithm = ""

		self.chosen_sequence = ""
		self.chosen_algorithm = ""


		# create listbox and scrollbar
		self.Lb = Listbox(self.list_frame, selectmode=EXTENDED, width = 100, relief=GROOVE)
		self.scrollbar = Scrollbar(self.list_frame)
		self.scrollbar.pack(side=RIGHT, fill=Y)

		# attach listbox to scrollbar
		self.Lb.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.Lb.yview)

		# create select button
		self.select_button = Button(self.top_frame, text=">> Select <<", relief=GROOVE)
		self.select_button.bind("<Button-1>", self.list_selection)

		# create sequence entry bar 
		self.label = Label(self.sequence_frame, text="Sequence:", font='Helvetica 12  bold')
		self.label.pack(pady=10)
		self.entry = Entry(self.sequence_frame, width = 100)
		self.entry.pack()

		# add checkboxes for algorithm
		self.var1 = IntVar()
		self.var1.set(0)
		self.algorithm_1 = Checkbutton(self.algo_frame, text="Random", variable = self.var1, command = self.check_box1)
		self.algorithm_1.grid(row = 0, column = 0)

		self.var2 = IntVar()
		self.var2.set(0)
		self.algorithm_2 = Checkbutton(self.algo_frame, text="Breadth-first", variable = self.var2, command = self.check_box2)
		self.algorithm_2.grid(row = 0, column = 1)

		self.var3 = IntVar()
		self.var3.set(0)
		self.algorithm_3 = Checkbutton(self.algo_frame, text="Depth-first", variable = self.var3, command = self.check_box3)
		self.algorithm_3.grid(row = 0, column = 2)


		# create fold button to continue
		self.continue_button = Button(self.algo_frame, text="Fold", bg="red", fg = "white")
		self.continue_button.bind("<Button-1>", self.get_sequence)
		self.continue_button.grid(row=1, column = 1, pady = 20, ipadx = 20, ipady = 5)


		# create status bar
		self.status = Label(self.root, text="", bd=1, relief=SUNKEN, anchor=W)
		self.status.pack(side=BOTTOM, fill = X)
	
	def check_box1(self):
		if(self.var1.get()):
			self.algorithm_1.config(state=DISABLED)
			self.var2.set(0)
			self.algorithm_2.config(state=NORMAL)
			self.var3.set(0)
			self.algorithm_3.config(state=NORMAL)

			self.selected_algorithm = "random"

	def check_box2(self):
		if(self.var2.get()):
			self.algorithm_2.config(state=DISABLED)
			self.var1.set(0)
			self.algorithm_1.config(state=NORMAL)
			self.var3.set(0)
			self.algorithm_3.config(state=NORMAL)

			self.selected_algorithm = "breadth"

	def check_box3(self): 
		if(self.var3.get()):
			self.algorithm_3.config(state=DISABLED)
			self.var1.set(0)
			self.algorithm_1.config(state=NORMAL)
			self.var2.set(0)
			self.algorithm_2.config(state=NORMAL)

			self.selected_algorithm = "depth"

	def list_load(self, sequences): 

		for i in range(0, len(sequences)): 
			self.Lb.insert(i, sequences[i]["sequence"])

		self.Lb.pack(fill = X)

		self.select_button.pack(fill = X)
		

	def list_selection(self, event):
		a = self.Lb.curselection()
		for i in a: 
			self.entry.delete(0, END)
			self.entry.insert(0, self.Lb.get(i))

	def get_sequence(self, event): 
		self.selected_sequence = self.entry.get()
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



