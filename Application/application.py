# Imports
import sys
import timeit
from Classes import AminoAcidChain
from Dependencies import helpers as h



# Main function.
def main():

	# initialize timer
	start = timeit.default_timer()

	# Check if command line argument is given.
	if (len(sys.argv) != 2):
		sys.exit("Usage: python program.py algorithm")

	algorithm = str(sys.argv[1])

	sequences = h.load_sequences_from_csv()
	
	sequence = h.select_sequence(sequences)

	# create AminoAcidChain object
	amino_acid_chain = AminoAcidChain.Amino_acid_chain()

	# Create amino acid chain by the given comment line argument.
	amino_acid_chain.create(sequence)

	# Set x and y coordinates of the aminoacids of chain.
	amino_acid_chain.fold(algorithm)

	# stop timer
	stop = timeit.default_timer()
	print("Runtime:", (stop - start))
	
	# calculate chains stability score
	score = amino_acid_chain.stability()
	print("Score:", (score))

	# Plot the "folded" aminoacid chain.
	amino_acid_chain.plot()

		
# Main execution
if __name__ == '__main__':
	main()
	