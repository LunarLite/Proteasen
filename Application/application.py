# Imports.
import sys

from Dependencies.helpers import *
from Classes.AminoAcid import *

# Global variables.
aminoacid_chain = []

# Main function.
def main():

	# Check if command line argument is given.
	if (len(sys.argv) != 2):
		sys.exit("Usage: python program.py HPPHHPPHH")

	input = str(sys.argv[1])
	
	# Create amino acid chain by the given comment line argument.
	aminoacid_chain = load(input)

	# Set x and y coordinates of the aminoacids of chain.
	fold(aminoacid_chain)

	# Plot the "folded" aminoacid chain.
	plot(aminoacid_chain)

		
# Main execution
if __name__ == '__main__':
	main()
	