# experiment.py
#
# plots data from csv file of type: 
# header 
# x, y
# x, y etc 
#

import matplotlib.pyplot as plt 
import csv


fig = plt.figure()

def main(): 

	x = []
	y = []

	with open("experiment3.csv", 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		firstline = True
		for row in reader: 
			if firstline: 
				firstline = False 
				continue 
			x.append(int(row[0]))
			y.append(int(row[1]))

		# print("x", x, "y", y)	

		plot(x, y)


def plot(x, y): 

	# Add new subplot
	subPlot = fig.add_subplot(111)

	subPlot.plot(x, y, 'k-')

	# draw a grid behind Subplot 
	subPlot.grid()

	# display pop-up window with plot
	plt.show()

	
if __name__ == '__main__':
	main()