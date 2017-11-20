from tkinter import *

class Sequence_Selector:
	def __init__(self, master): 
		# set window
		self.root = master
		self.root.title("Enter Sequence")
		self.root.geometry("900x500")
		self.container = Frame(self.root)
		self.container.pack()
		self.select_frame = Frame(self.container)
		self.select_frame.grid(row=0)
		self.sequence_frame = Frame(self.container)
		self.sequence_frame.grid(row=2, padx=10, pady=20)

		# default mode selected sequence
		self.selected_sequence = ""


		# create listbox
		self.Lb = Listbox(self.select_frame, selectmode=EXTENDED, width = 100, relief=GROOVE)
		

		#create buttons
		self.select_button = Button(self.select_frame, text=">> Select <<", relief=GROOVE)
		self.select_button.bind("<Button-1>", self.selection)
		
		

		# create textbar
		self.label = Label(self.sequence_frame, text="Sequence:", font='Helvetica 12  bold')
		self.label.pack()
	
		self.entry = Entry(self.sequence_frame, width = 100)
		self.entry.pack()

		#
		# FUNCTIONALITEIT TOEVOEGEN
		#

		# add checkboxes for algorithm
		self.algorithm_1 = Checkbutton(self.sequence_frame, text="Random", variable="random")
		self.algorithm_2 = Checkbutton(self.sequence_frame, text="Breadth-first", variable="breadth")
		self.algorithm_3 = Checkbutton(self.sequence_frame, text="Depth-first", variable="depth")
		self.algorithm_1.pack(side = TOP, anchor = CENTER)
		self.algorithm_2.pack(side = TOP, anchor = CENTER)
		self.algorithm_3.pack(side = TOP, anchor = CENTER)


		# create continue button
		self.continue_button = Button(self.sequence_frame, text="Fold", bg="red", fg = "white")
		self.continue_button.bind("<Button-1>", self.get_sequence)
		self.continue_button.pack()


		# create status bar
		self.status = Label(self.root, text="", bd=1, relief=SUNKEN, anchor=W)
		self.status.pack(side=BOTTOM, fill = X)
	
	def load_list(self, sequences): 

		for i in range(0, len(sequences)): 
			self.Lb.insert(i, sequences[i]["sequence"])

		self.Lb.pack(fill = X)

		self.select_button.pack(fill = X)
		

	def selection(self, event):
		a = self.Lb.curselection()
		for i in a: 
			self.entry.delete(0, END)
			self.entry.insert(0, self.Lb.get(i))

	def get_sequence(self, event): 
		self.selected_sequence = self.entry.get()
		if self.validate():
			self.root.quit()
			self.root.withdraw()

	def validate(self): 
		if self.selected_sequence == "":
			self.status["text"] = "Warning: sequence invalid"
			return False

		# Ensure sequence contains only H and P
		self.selected_sequence = self.selected_sequence.strip()
		for c in self.selected_sequence:
			if (c.upper() != 'H' and c.upper() != 'P'):
				self.status["text"] = "Warning: sequence must contain only H and P"
				return False

		else: return True



