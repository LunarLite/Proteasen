# Imports.
from random import randint
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
	fold()

	# Plot the "folded" aminoacid chain.
	plot()



# Determines optimal aminoacid chain configuration.
def fold(): 

	# Iterate over each aminoacid.
	for i in range (1, len(aminoacid_chain)):

		# create array containing possible positions
		prev_acid = aminoacid_chain[i - 1]
		tup1 = [prev_acid.x + 1, prev_acid.y]
		tup2 = [prev_acid.x - 1, prev_acid.y]
		tup3 = [prev_acid.x, prev_acid.y + 1]
		tup4 = [prev_acid.x, prev_acid.y - 1]

		options = [tup1, tup2, tup3, tup4]

		zelfde = True
		fouten = []
		fout = True

		while zelfde:
			zelfde = False

			while fout:
				option = randint(0, 3)
				if option not in fouten:
					fout = False

			x = options[option][0]
			y = options[option][1]

			for j in range(0, i - 1):
				if aminoacid_chain[j].x == x and aminoacid_chain[j].y == y:
			 		zelfde = True
			 		fouten.append(option)
			 		break
			 	else: 
			 		zelfde = False
			 		fouten = 0
			 		

		print(x, y)

		aminoacid_chain[i].x = x
		aminoacid_chain[i].y = y
		
# Main execution
if __name__ == '__main__':
	main()
	