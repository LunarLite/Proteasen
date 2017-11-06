# imports
import sys

# global variables
dict_of_molecules = {}


# Molecule. Can be either hydrophobic or polair, gets a position assigned based on the algorythm
class Amino_acid:
	def __init__(self, molecule_type):
		self.molecule_type = molecule_type

def load(input):
	count = 0
	for c in input:
		x = str(count)
		count += 1
		if (c.upper() == 'H'):
			molecule_type = "hydrophobic"
		else:
			molecule_type = "polair"
		dict_of_molecules[x] = Amino_acid(molecule_type)
		
# main execution
if __name__ == '__main__':
	# check given input
	if (len(sys.argv) != 2):
		sys.exit("Usage: python program.py HPPHHPPHH")
	input = str(sys.argv[1])
	
	# load the argv into molecule dict
	load(input)
	

		
	# check contents on name and type
	for x in dict_of_molecules:
		print str(x)
		print str(dict_of_molecules[x].molecule_type)