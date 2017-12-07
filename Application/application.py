# imports
from random import randint
import sys
import timeit

from Classes import AminoAcidChain, GuiApplication
from Algorithms import random_algorithm, breadth_algorithm, breadthh_algorithm, hillclimber_algorithm
from Dependencies import helpers


# main function
def main():

	if len(sys.argv) == 3: 
		algorithm = sys.argv[1]
		sequence = sys.argv[2]

	elif len(sys.argv) > 1: 
		sys.exit("\nUsage: application.py algorithm HHPHHHPHPHHHPH\n"
					"algorithms: Random/Breadth/Breadth_heur/Hillclimber/Randomhillclimber\n")
		
	else: 
		app = GuiApplication.Gui_Application()
		app.run("csv", "sequences.csv")
		sequence = app.get("sequence")
		algorithm = app.get("algorithm")

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
		hillclimber_algorithm.execute(amino_acid_chain, "straight_folded")
	elif algorithm == "Randomhillclimber" or algorithm == "randomhillclimber":
		hillclimber_algorithm.execute(amino_acid_chain, "random_folded")
	else: 
		sys.exit("\nUsage: application.py algorithm HHPHHHPHPHHHPH\n"
					"algorithms: Random/Breadth/Breadth_heur/Hillclimber/Randomhillclimber\n")
	
	# stop timer
	stop = timeit.default_timer()
	print("Runtime:", (stop - start))
	
	# calculate chains stability score
	amino_acid_chain.stability()
	print("Score:", (amino_acid_chain.score))

	# plot the "folded" aminoacid chain
	amino_acid_chain.plot()

		
# main execution
if __name__ == '__main__':
	main()
	