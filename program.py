# Imports.
from matplotlib import pyplot as plt
from random import randint
import sys

# Global variables.
aminoacid_chain = []

# Aminoacid. 
# Can be either hydrophobic or polair.
# Gets a position assigned based on the algorythm.
class Amino_acid:
	def __init__(self, molecule_type):
		self.molecule_type = molecule_type
		self.x = 0
		self.y = 0

# Main function.
def main():

	# Check if command line argument is given.
	if (len(sys.argv) != 2):
		sys.exit("Usage: python program.py HPPHHPPHH")

	input = str(sys.argv[1])
	
	# Create amino acid chain by the given comment line argument.
	load(input)

	# Set x and y coordinates of the aminoacids of chain.
	fold()

	# Plot the "folded" aminoacid chain.
	plot()
		
	# Check contents on name and type.
	for i in range(0, len(aminoacid_chain)):
		print str(i)
		print str(aminoacid_chain[i].molecule_type)


# Creates a list of aminoacids by given comment line argument consisting of H and P.
# Returns error when comment line argument contains characters other than H or P. 
def load(input):

	# Iterate over each character in command line argument. 
	for c in input:

		# Allow only H and P in command line argument. 
		# Set molecule type to either hydrophobic or polair, as H or P indicates.
		if (c.upper() == 'H'):
			molecule_type = "hydrophobic"

		elif (c.upper() == 'P'):
			molecule_type = "polair"

		else: 
			sys.exit("Usage: python program.py HPPHHPPHH")

		# Create aminoacid with appropriate type and append it to the chain.
		aminoacid_chain.append(Amino_acid(molecule_type))


# Plots aminoacid chain configuration.
def plot():
	
	# Create empty lists to store x and y coordinates.
	x = []
	y = []

	# Iterate over each aminoacid. 
	for i in range(0, len(aminoacid_chain)):

		# Store x and y coordinates of current aminoacid.
		x.append(aminoacid_chain[i].x)
		y.append(aminoacid_chain[i].y)
	
	# Plot backbone aminoacid chain.
	plt.plot(x, y, 'k-')

	# Iterate over each aminoacid.
	for i in range(0, len(aminoacid_chain)):
		
		# Check for type of current aminoacid. 
		if aminoacid_chain[i].molecule_type == "hydrophobic": 

			# Plot red dot at coordinates of hydrophobic aminoacid.
			plt.plot(aminoacid_chain[i].x, aminoacid_chain[i].y, 'ro')

		elif aminoacid_chain[i].molecule_type == "polair":  

			# Plot blue dot at coordinates of polair aminoacid.
			plt.plot(aminoacid_chain[i].x, aminoacid_chain[i].y, 'bo')
	
	# Draw a grid behind plots. 
	plt.grid()

	# Display pop-up window with plot. 
	plt.show()

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
	