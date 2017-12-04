# imports
import sys
import timeit
from Classes import AminoAcidChain
from Visualisation import visualisation



# main function
def main():

	if len(sys.argv) == 3: 
		algorithm = sys.argv[1]
		sequence = sys.argv[2]

	elif len(sys.argv) > 1: 
		sys.exit("Usage: application.py algorithm HHPHHHPHPHHHPH") 
		
	else: 
		sequence, algorithm = visualisation.run()

	
	# initialize timer
	start = timeit.default_timer()
		
	# create AminoAcidChain object
	amino_acid_chain = AminoAcidChain.Amino_acid_chain()

	# create amino acid chain by the given comment line argument
	amino_acid_chain.create(sequence)
	
	# set x and y coordinates of the aminoacids of chain
	amino_acid_chain.execute(algorithm)

	# stop timer
	stop = timeit.default_timer()
	print("Runtime:", (stop - start))
	
	# calculate chains stability score
	score = amino_acid_chain.stability()
	print("Score:", (score))

	# plot the "folded" aminoacid chain
	amino_acid_chain.plot()

		
# main execution
if __name__ == '__main__':
	main()
	