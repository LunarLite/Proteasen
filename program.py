# Imports.
from matplotlib import pyplot as plt
from random import randint
import sys

# Global variables.
dict_of_molecules = {}


# Molecule. 
# Can be either hydrophobic or polair, gets a position assigned based on the algorythm.
class Amino_acid:
	def __init__(self, molecule_type, x, y):
		self.molecule_type = molecule_type
		self.x = x
		self.y = y

def main():

	# Check given input.
	if (len(sys.argv) != 2):
		sys.exit("Usage: python program.py HPPHHPPHH")
	input = str(sys.argv[1])
	
	# Load the argv into molecule dict.
	load(input)
	plot()
	
		
	# Check contents on name and type.
	for x in dict_of_molecules:
		print str(x)
		print str(dict_of_molecules[x].molecule_type)

# Loads aminoacid chain.
def load(input):
	count = 0
	for c in input:
		x = str(count)
		count += 1
		if (c.upper() == 'H'):
			molecule_type = "hydrophobic"
		else:
			molecule_type = "polair"
		dict_of_molecules[x] = Amino_acid(molecule_type, randint(0, 9), randint(0, 9))

# Plots optimal peptide chain configuration.
def plot():
	
	# Create empty list to store coordinates.
	x = []
	y = []

	# Iterate over each aminoacid in dictionary. 
	for i in dict_of_molecules:

		# Store coordinates of current aminoacid in list.
		x.append(dict_of_molecules[i].x)
		y.append(dict_of_molecules[i].y)
	
	# Plot backbone aminoacid chain.
	plt.plot(x, y, 'k-')

	# Iterate over each aminoacid in dictionary.
	for i in dict_of_molecules:
		
		# Check for type of current aminoacid. 
		if dict_of_molecules[i].molecule_type == "hydrophobic": 

			# Plot red dot at coordinates of hydrophobic aminoacid.
			plt.plot(dict_of_molecules[i].x, dict_of_molecules[i].y, 'ro')

		elif dict_of_molecules[i].molecule_type == "polair":  

			# Plot blue dot at coordinates of polair aminoacid.
			plt.plot(dict_of_molecules[i].x, dict_of_molecules[i].y, 'bo')
	
	# Draw a grid behind plots. 
	plt.grid()

	# Display pop-up window with plot. 
	plt.show()

		
# Main execution
if __name__ == '__main__':
	main()
	