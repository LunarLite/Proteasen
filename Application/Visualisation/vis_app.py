import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt

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
		
		# create listbox and scrollbar
		self.listbox = tk.Listbox(self, selectmode = tk.EXTENDED, width = 100, relief = tk.GROOVE)
		self.listbox.pack(fill = tk.X)
		self.listbox.insert(0, "No sequences available") #help implementeren die laat zien hoe je sequenties in kan laden
		self.listbox.delete(0)
		self.load_listbox(["HPPHPHHH", "HPHPHHHPHPPHH", "hPHHPHPPHPHPH", "HPPHPHPHPPH"])

		self.scrollbar = tk.Scrollbar(self)
		self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

		# attach listbox to scrollbar
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

		self.var1 = tk.IntVar()
		self.var1.set(0)
		self.checkbutton1 = tk.Checkbutton(self, text="Random", variable = self.var1, command = self.select_1)
		# checkbutton1.grid(row = 0, column = 0)
		self.checkbutton1.pack()

		self.var2 = tk.IntVar()
		self.var2.set(0)
		self.checkbutton2 = tk.Checkbutton(self, text="Breadth-first", variable = self.var2, command = self.select_2)
		# checkbutton2.grid(row = 0, column = 1)
		self.checkbutton2.pack()

		self.var3 = tk.IntVar()
		self.var3.set(0)
		self.checkbutton3 = tk.Checkbutton(self, text="Depth-first", variable = self.var3, command = self.select_3)
		# checkbutton3.grid(row = 0, column = 2)
		self.checkbutton3.pack()


		# create fold button to continue
		button2 = ttk.Button(self, text="Fold")
		# continue_button.bind("<Button-1>", self.get)
		button2.pack(pady=10, padx=10)
		# continue_button.grid(row=1, column = 1, pady = 20, ipadx = 20, ipady = 5)


		# create status bar
		self.status = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
		self.status.pack(side = tk.BOTTOM, fill = tk.X)
	

	def load_listbox(self, sequences):

		for i in range(0, len(sequences)): 
			self.listbox.insert(i, sequences[i])


	def select_from_listbox(self, event):
		a = self.listbox.curselection()
		for i in a: 
			self.entry.delete(0, tk.END)
			self.entry.insert(0, self.listbox.get(i))

	def select_1(self):
		if(self.var1.get()):
			self.checkbutton1.config(state=tk.DISABLED)
			self.var2.set(0)
			self.checkbutton2.config(state=tk.NORMAL)
			self.var3.set(0)
			self.checkbutton3.config(state=tk.NORMAL)

			# self.selected_algorithm = "random"

	def select_2(self):
		if(self.var2.get()):
			self.checkbutton2.config(state=tk.DISABLED)
			self.var1.set(0)
			self.checkbutton1.config(state=tk.NORMAL)
			self.var3.set(0)
			self.checkbutton3.config(state=tk.NORMAL)

			# self.selected_algorithm = "breadth"

	def select_3(self): 
		if(self.var3.get()):
			self.checkbutton3.config(state=tk.DISABLED)
			self.var1.set(0)
			self.checkbutton1.config(state=tk.NORMAL)
			self.var2.set(0)
			self.checkbutton2.config(state=tk.NORMAL)

			# self.selected_algorithm = "depth"



class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="This algorithm will have a runtime of aprox. "+ "add_runtime" + " seconds", font=MEDIUM_FONT)
		label.pack(pady=10, padx=10)

		label = ttk.Label(self, text="Are you sure you want to continue?", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text="Yes", command=lambda: controller.show_frame(PageTwo))
		button1.pack()

		button2 = ttk.Button(self, text="No", command=lambda: controller.show_frame(StartPage))
		button2.pack()



# https://www.youtube.com/watch?v=Zw6M-BnAPP0&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=6
class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
		button1.pack()


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