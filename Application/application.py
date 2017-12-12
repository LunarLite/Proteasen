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
from random import randint
import sys
import timeit

from Classes import AminoAcidChain, GuiApplication
from Algorithms import random_algorithm, breadth_algorithm, breadthh_algorithm, hillclimber_algorithm, hillclimber_algorithm3D, simulated_annealing
from Dependencies import helpers


# main function
def main():

	if len(sys.argv) == 4: 
		dimension = sys.argv[1]
		algorithm = sys.argv[2]
		sequence = sys.argv[3]

		if dimension != "2D" and dimension != "3D" and dimension != "2d" and dimension != "3d": 
			sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Hillclimber / Randomhillclimber / Simulatedannealing\n")


		# if iterative algorithm, ask user to input number of iterations
		if (algorithm == "Hillclimber" or 
			algorithm == "hillclimber" or 
			algorithm == "Randomhillclimber" or 
			algorithm == "randomhillclimber" or 
			algorithm == "Simulatedannealing" or
			algorithm == "simulatedannealing"):
			iterations = helpers.ask_for_iterations()


	elif len(sys.argv) > 1: 
		sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Hillclimber / Randomhillclimber / Simulatedannealing\n")
		
	else: 
		app = GuiApplication.Gui_Application()
		app.run("csv", "Data/sequences.csv")
		sequence = app.get("sequence")
		algorithm = app.get("algorithm")
		if algorithm == "Hillclimber" or algorithm == "Randomhillclimber":
			iterations = app.get("iterations")
		dimension = "2D"

	# initialize timer
	start = timeit.default_timer()
		
	# create AminoAcidChain object
	amino_acid_chain = AminoAcidChain.Amino_acid_chain(sequence)
	
		
	# set x and y coordinates of the aminoacids of chain, depending on the algorithm	
	if algorithm == "Random" or algorithm == "random":
		random_algorithm.execute(amino_acid_chain)
	# ensure proper usage
	elif algorithm == "Breadth" or algorithm == "breadth" or algorithm == "Breadth-first":
		breadth_algorithm.execute(amino_acid_chain)
	elif algorithm == "Breadth_heur" or algorithm == "breadth_heur":
		breadthh_algorithm.execute(amino_acid_chain)
	elif algorithm == "Hillclimber" or algorithm == "hillclimber":
		if dimension == "2D": 
			hillclimber_algorithm.execute(amino_acid_chain, "straight_folded", iterations)
		elif dimension == "3D": 
			hillclimber_algorithm3D.execute(amino_acid_chain, "straight_folded", iterations)
	elif algorithm == "Randomhillclimber" or algorithm == "randomhillclimber":
		if dimension == "2D": 
			hillclimber_algorithm.execute(amino_acid_chain, "straight_folded", iterations)
		elif dimension == "3D": 
			hillclimber_algorithm3D.execute(amino_acid_chain, "random_folded", iterations)
	elif algorithm == "Simulatedannealing" or algorithm == "simulatedannealing":
		if dimension == "2D": 
			simulated_annealing.execute(amino_acid_chain, "straight_folded", iterations)
		elif dimension == "3D": 
			simulated_annealing.execute(amino_acid_chain, "random_folded", iterations)
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

		
# main execution
if __name__ == '__main__':
	main()
	