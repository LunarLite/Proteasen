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

	x4 = []
	y4 = []

	x5 = []
	y5 = []

	x6 = []
	y6 = []

	with open("straight_hill_exp_3d.csv", 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		firstline = True
		for row in reader: 
			if firstline: 
				firstline = False 
				continue 
			x1.append(float(row[0]))
			y1.append(int(row[1]))

	with open("depth_hill_exp_3d.csv", 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		firstline = True
		for row in reader: 
			if firstline: 
				firstline = False 
				continue 
			x2.append(float(row[0]))
			y2.append(int(row[1]))

	with open("random_hill_exp_3d.csv", 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		firstline = True
		for row in reader: 
			if firstline: 
				firstline = False 
				continue 
			x3.append(float(row[0]))
			y3.append(int(row[1]))

	with open("straight_siman_exp_3d.csv", "r") as csvfile:
		reader = csv.reader(csvfile, delimiter=",")

		firstline = True
		for row in reader:
			if firstline:
				firstline = False
				continue
			x4.append(float(row[0]))
			y4.append(int(row[1]))

	with open("random_exp_3d.csv", "r") as csvfile:
		reader = csv.reader(csvfile, delimiter=",")

		firstline = True
		for row in reader:
			if firstline:
				firstline = False
				continue
			x5.append(float(row[0]))
			y5.append(int(row[1]))

	with open("random_siman_exp_3d.csv", "r") as csvfile:
		reader = csv.reader(csvfile, delimiter=",")

		firstline = True
		for row in reader:
			if firstline:
				firstline = False
				continue
			x6.append(float(row[0]))
			y6.append(int(row[1]))


		plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)


def plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6): 

	# Add new subplot
	subPlot = fig.add_subplot(111)

	subPlot.plot(x1, y1, 'r.')
	subPlot.plot(x2, y2, 'b.')
	subPlot.plot(x3, y3, 'g.')
	subPlot.plot(x4, y4, 'm.')
	subPlot.plot(x5, y5, 'c.')
	subPlot.plot(x6, y6, 'y.')


	# draw a grid behind Subplot 
	subPlot.grid()

	# display pop-up window with plot
	plt.show()

	
if __name__ == '__main__':
	main()