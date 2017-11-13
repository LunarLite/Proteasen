# Imports.
import sys
import timeit
from Classes import AminoAcidChain

# Main function.
def main():

	# initialize timer
	start = timeit.default_timer()

	# Check if command line argument is given.
	if (len(sys.argv) != 3):
		sys.exit("Usage: python program.py HPPHHPPHH algorithm")

	input = str(sys.argv[1])
	
	# create AminoAcidChain object
	amino_acid_chain = AminoAcidChain.Amino_acid_chain()

	# Create amino acid chain by the given comment line argument.
	amino_acid_chain.create(input)

	# Set x and y coordinates of the aminoacids of chain.
	amino_acid_chain.fold()

	# stop timer
	stop = timeit.default_timer()
	print"Runtime:", (stop - start)
	
	# Plot the "folded" aminoacid chain.
	amino_acid_chain.plot()

		
# Main execution
if __name__ == '__main__':
	main()
	