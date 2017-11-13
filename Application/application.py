# Imports.
import sys
import timeit

from Dependencies import helpers as h

# Main function.
def main():

	# initialize timer
	start = timeit.default_timer()

	# Check if command line argument is given.
	if (len(sys.argv) != 2):
		sys.exit("Usage: python program.py HPPHHPPHH")

	input = str(sys.argv[1])
	
	# Create amino acid chain by the given comment line argument.
	amino_acid_chain = h.load(input)

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
	