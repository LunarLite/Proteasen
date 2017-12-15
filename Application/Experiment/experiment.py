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

	x1 = []
	y1 = []

	x2 = []
	y2 = []

	x3 = []
	y3 = []

	with open("exp10.csv", 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		firstline = True
		for row in reader: 
			if firstline: 
				firstline = False 
				continue 
			x1.append(int(row[0]))
			y1.append(int(row[1]))

	with open("exp9.csv", 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		firstline = True
		for row in reader: 
			if firstline: 
				firstline = False 
				continue 
			x2.append(int(row[0]))
			y2.append(int(row[1]))

	with open("exp11.csv", 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		firstline = True
		for row in reader: 
			if firstline: 
				firstline = False 
				continue 
			x3.append(int(row[0]))
			y3.append(int(row[1]))

		plot(x1, y1, x2, y2, x3, y3)


def plot(x1, y1, x2, y2, x3, y3): 

	# Add new subplot
	subPlot = fig.add_subplot(111)

	subPlot.plot(x2, y2, 'b-')
	subPlot.plot(x1, y1, 'r-')
	subPlot.plot(x3, y3, 'g-')


	# draw a grid behind Subplot 
	subPlot.grid()

	# display pop-up window with plot
	plt.show()

	
if __name__ == '__main__':
	main()