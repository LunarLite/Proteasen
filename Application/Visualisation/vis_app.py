import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt

from Classes import AminoAcidChain

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


style.use("ggplot")


f = Figure()
a = f.add_subplot(111)

def animate(i): 
	pullData = open("sampleData.txt", "r").read()
	dataList = pullData.split('\n')
	xList = []
	yList = []
	for eachLine in dataList:
		if len(eachLine) > 1: 
			x, y =eachLine.split(',')
			xList.append(int(x))
			yList.append(int(y))

	a.clear()
	a.plot(xList, yList)

class Visualisation_App(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		# tk.Tk.iconbitmap(self, default="clienticon.ico")
		tk.Tk.wm_title(self, "Protein Po(w)der")
		tk.Tk.resizable(self, width = tk.FALSE, height = tk.FALSE)

		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight =1)

		self.frames = {}
		for F in (StartPage, PageOne, PageTwo, GuiPage):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont): 

		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame): 

	def __init__(self,parent, controller): 

		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="StartPage", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text="Warning page", command=lambda: controller.show_frame(PageOne))
		button1.pack()

		button2 = ttk.Button(self, text="Graph page", command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = ttk.Button(self, text="Gui page", command=lambda: controller.show_frame(GuiPage))
		button3.pack()


class GuiPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		
		list_frame = tk.Frame(self)
		list_frame.pack(side=tk.TOP, fill = tk.X)
		
		# create listbox and scrollbar
		self.scrollbar = tk.Scrollbar(list_frame)
		self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

		self.listbox = tk.Listbox(list_frame, selectmode = tk.EXTENDED, width = 100, relief = tk.GROOVE)
		self.listbox.pack(fill = tk.X)
		self.listbox.insert(0, "No sequences available") #help implementeren die laat zien hoe je sequenties in kan laden
		self.listbox.delete(0)
		self.load_listbox(["HPPHPHHH", "HPHPHHHPHPPHH", "hPHHPHPPHPHPH", "HPPHPHPHPPH"])

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
		checkbutton1 = ttk.Checkbutton(check_frame, text="Random", variable = var1, command=lambda: self.check("Random"))
		checkbutton1.grid(row = 0, column = 0)
		self.checkbuttons["Random"] = {"button": checkbutton1, "var": var1}

		var2 = tk.IntVar()
		var2.set(0)
		checkbutton2 = ttk.Checkbutton(check_frame, text="Breadth-first", variable = var2, command=lambda: self.check("Breadth-first"))
		checkbutton2.grid(row = 0, column = 1)
		self.checkbuttons["Breadth-first"] = {"button": checkbutton2, "var": var2}

		var3 = tk.IntVar()
		var3.set(0)
		checkbutton3 = ttk.Checkbutton(check_frame, text="Depth-first", variable = var3, command=lambda: self.check("Depth-first"))
		checkbutton3.grid(row = 0, column = 2)
		self.checkbuttons["Depth-first"] = {"button": checkbutton3, "var": var3}


		# create fold button to continue
		button2 = ttk.Button(self, text="Fold", command=lambda: self.validate(controller))
		button2.pack(pady=10, padx=10)

		# create status bar
		self.status = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=SMALL_FONT)
		self.status.pack(side = tk.BOTTOM, fill = tk.X)
	

	def load_listbox(self, sequences):

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

	def validate(self, controller):

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

		if self.get("algorithm") == "Depth-first":
			self.status["text"] = "Warning: depth-first is not implemented yet"
			return False

		# else: return True
		else: controller.show_frame(PageOne)


	def get(self, g):

		if g == "algorithm": 
			for i in self.checkbuttons:
				if self.checkbuttons[i]["var"].get() == 1:
					return i

		elif g == "sequence":
			return self.entry.get()

class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		warning_frame = tk.Frame(self)
		warning_frame.pack(pady=100)
		button_frame = tk.Frame(warning_frame)
		button_frame.pack(side=tk.BOTTOM, pady=10)

		label = ttk.Label(warning_frame, text="This algorithm will have a runtime of aprox. "+ "add_runtime" + " seconds", font=MEDIUM_FONT)
		label.pack(pady=10, padx=10)

		label = ttk.Label(warning_frame, text="Are you sure you want to continue?", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(button_frame, text="Yes", command=lambda: controller.show_frame(PageTwo))
		button1.grid(row=0, column=0)

		button2 = ttk.Button(button_frame, text="No", command=lambda: controller.show_frame(StartPage))
		button2.grid(row=0, column=1)

	def run_algorithm(self): 
		# create AminoAcidChain object
		amino_acid_chain = AminoAcidChain.Amino_acid_chain()

		# create amino acid chain by the given comment line argument
		# amino_acid_chain.create(get("sequence"))
	
		# set x and y coordinates of the aminoacids of chain
		# amino_acid_chain.execute(get("algorithm"))

		get("sequence")

# https://www.youtube.com/watch?v=Zw6M-BnAPP0&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=6
class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="Results", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		label = ttk.Label(self, text="Score: "+"add_score", font=MEDIUM_FONT)
		label.pack(pady=2, padx=10)

		label = ttk.Label(self, text="Runtime: "+"add_runtime", font=MEDIUM_FONT)
		label.pack(pady=2, padx=10)

		button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
		button1.pack(pady=4)


		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = Visualisation_App()
app.geometry("800x700")
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()