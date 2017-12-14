# experiment.py
#
# plots data from csv file of type: 
# header 
# x, y
# x, y etc 
#

import matplotlib.pyplot as plt 
import sys
import timeit

from Classes import AminoAcidChain, GuiApplication
from Algorithms import random_algorithm, breadth_algorithm, breadthh_algorithm, depth_algorithm, hillclimber_algorithm, hillclimber_algorithm3D, simulated_annealing
from Dependencies import helpers

fig = plt.figure()

def main(): 


	if len(sys.argv) == 4: 
		dimension = sys.argv[1].lower()
		algorithm = sys.argv[2].lower()
		sequence = sys.argv[3].lower()

		if dimension != "2d" and dimension != "3d": 
			sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / hillclimber / Randomhillclimber / Simulatedannealing\n")


		# if iterative algorithm, ask user to input number of iterations
		if (algorithm == "hillclimber" or 
			algorithm == "randomhillclimber" or 
			algorithm == "simulatedannealing"):
			iterations = helpers.ask_for_iterations()

		elif algorithm == "depth":
			depth_hill = input("Would you like to perform hillclimbing after DFS? (y/n)")



	elif len(sys.argv) > 1: 
		sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Hillclimber / Randomhillclimber / Simulatedannealing\n")
		
	else: 
		app = GuiApplication.Gui_Application()
		app.run("csv", "Data/sequences.csv")
		sequence = app.get("sequence")
		algorithm = app.get("algorithm").lower()
		if algorithm == "hillclimber" or algorithm == "randomhillclimber":
			iterations = app.get("iterations")
		dimension = "2d"

	# initialize timer
	start = timeit.default_timer()
		
	# create AminoAcidChain object
	amino_acid_chain = AminoAcidChain.Amino_acid_chain(sequence)
	
	# set x and y coordinates of the aminoacids of chain, depending on the algorithm	
	if algorithm == "random":
		random_algorithm.execute(amino_acid_chain)
	# breadth-first
	elif algorithm == "breadth" or algorithm == "breadth-first":
		breadth_algorithm.execute(amino_acid_chain, dimension)
	# breadth-first with heuristics
	elif algorithm == "breadth_heur":
		breadthh_algorithm.execute(amino_acid_chain, dimension)
	# depth-first
	elif algorithm == "depth":
		max_duration = 15
		finished = depth_algorithm.execute(amino_acid_chain, dimension, max_duration)
		if depth_hill == "y" and finished == False:
			amino_acid_chain.stability()
			print("Performing hillclimber.. Current score: ", amino_acid_chain.score)
			hillclimber_algorithm.execute(amino_acid_chain, "dept_chain", 500, dimension)
	# hillclimber
	elif algorithm == "hillclimber":
		hillclimber_algorithm.execute(amino_acid_chain, "straight_folded", iterations, dimension)
	# hillclimber with random start
	elif algorithm == "randomhillclimber":
		hillclimber_algorithm.execute(amino_acid_chain, "random_folded", iterations, dimension)
	# simulated annealing
	elif algorithm == "simulatedannealing":
		if dimension == "2d": 
			simulated_annealing.execute(amino_acid_chain, "straight_folded", iterations)
		else:
			simulated_annealing.execute(amino_acid_chain, "random_folded", iterations)
	# non-valid commandline arg		
	else: 
		sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Hillclimber / Randomhillclimber / Simulatedannealing\n")


	# stop timer
	stop = timeit.default_timer()
	print("Runtime:", (stop - start))
	
	# calculate chains stability score
	amino_acid_chain.stability()
	print("Score:", (amino_acid_chain.score))

	# plot the "folded" aminoacid chain
	amino_acid_chain.plot(dimension)





	x = []
	y = []

	with open("test.csv", 'r') as csvfile:
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