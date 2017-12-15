# application.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the main script of the program 
# Usage: 
# > application.py algorithm HHPHHHPHPHH
#   algorithms: Random / Breadth / Breadth_heur / Hillclimber / Randomhillclimber 
# 
# > application.py (without command line arguments) to start GUI application



# imports
import sys
import timeit

from Classes import AminoAcidChain, GuiApplication
from Algorithms import random_algorithm, breadth_algorithm, breadthh_algorithm, depth_algorithm, hillclimber_algorithm, hillclimber_algorithm3D, simulated_annealing
from Dependencies import helpers


# main function
def main():

	if len(sys.argv) == 4: 
		dimension = sys.argv[1].lower()
		algorithm = sys.argv[2].lower()
		sequence = sys.argv[3].lower()

		if dimension != "2d" and dimension != "3d": 
			sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Depth / Randomhillclimber / Simulatedannealing\n")


		# if iterative algorithm, ask user to input number of iterations
		if (algorithm == "hillclimber" or 
			algorithm == "randomhillclimber" or 
			algorithm == "simulatedannealing" or
			algorithm == "randomsimulatedannealing" or
			algorithm == "random"):
			iterations = helpers.ask_for_iterations()

		elif algorithm == "depth":
			algorithm = helpers.ask_for_hillclimbing()



	elif len(sys.argv) > 1: 
		sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Depth / Depth_hill / Hillclimber / Randomhillclimber / Simulatedannealing / RandomSimulatedannealing\n")
		
	else: 
		app = GuiApplication.Gui_Application()
		app.run("csv", "Data/sequences.csv")
		specs = app.specs()

		print("\n", specs, "\n")

		sequence = specs["sequence"]
		algorithm = specs["algorithm"]
		dimension = specs["dimension"]

		print(algorithm)

		if (algorithm == "hillclimber" or 
			algorithm == "randomhillclimber" or 
			algorithm == "simulatedannealing" or
			algorithm == "randomsimulatedannealing" or
			algorithm == "random"):
			iterations = specs["iterations"]

		

	# initialize timer
	start = timeit.default_timer()
		
	# create AminoAcidChain object
	amino_acid_chain = AminoAcidChain.Amino_acid_chain(sequence)
	
		
	# set x and y coordinates of the aminoacids of chain, depending on the algorithm	
	if algorithm == "random":
		random_algorithm.execute(amino_acid_chain, iterations, dimension)
	# breadth-first
	elif algorithm == "breadth":
		breadth_algorithm.execute(amino_acid_chain, dimension)
	# breadth-first with heuristics
	elif algorithm == "breadth_heur":
		breadthh_algorithm.execute(amino_acid_chain, dimension)
	# depth-first
	elif algorithm == "depth" or algorithm == "depth_hill":
		max_duration = 15
		finished = depth_algorithm.execute(amino_acid_chain, dimension, max_duration)
		if algorithm == "depth_hill" and finished == False:
			amino_acid_chain.stability()
			print("Performing hillclimber.. Current score: ", amino_acid_chain.score)
			hillclimber_algorithm.execute(amino_acid_chain, "dept_chain", 1000, dimension)
	# hillclimber
	elif algorithm == "hillclimber":
		hillclimber_algorithm.execute(amino_acid_chain, "straight_folded", iterations, dimension)
	# hillclimber with random start
	elif algorithm == "randomhillclimber":
		hillclimber_algorithm.execute(amino_acid_chain, "random_folded", iterations, dimension)
	# simulated annealing
	elif algorithm == "simulatedannealing":
		simulated_annealing.execute(amino_acid_chain, "straight_folded", iterations, dimension)
	# simulated annealing with random start
	elif algorithm == "randomsimulatedannealing":
		simulated_annealing.execute(amino_acid_chain, "random_folded", iterations, dimension)
	# invalid commandline arg		
	else: 
		sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Depth / Depth_hill / Hillclimber / Randomhillclimber / Simulatedannealing / RandomSimulatedannealing\n")
	
	# stop timer
	stop = timeit.default_timer()
	print("Runtime:", (stop - start))
	
	# calculate chains stability score
	amino_acid_chain.stability()
	print("Score:", (amino_acid_chain.score))

	# plot the "folded" aminoacid chain
	amino_acid_chain.plot(dimension)

		
# main execution
if __name__ == '__main__':
	main()
	