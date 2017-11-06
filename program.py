# imports
import sys

# global variables
dictOfMolecules = {}


# Molecule. Can be either hydrophobic or polair, gets a position assigned based on the algorythm
class Aminozuur:
	def __init__(self, molecule_type):
		self.molecule_type = molecule_type

# main execution
if __name__ == '__main__':

	# check given input
	if (len(sys.argv) != 2):
		sys.exit("Usage: python program.py HPPHHPPHH")
	input = str(sys.argv[1])
	
	
	count = 0
	for c in input:
		x = str(count)
		count += 1
		if (c.upper() == 'H'):
			molecule_type = "hydrophobic"
		else:
			molecule_type = "polair"
		dictOfMolecules[x] = Aminozuur(molecule_type)
		
	# check contents on name and type
	for x in dictOfMolecules:
		print str(x)
		print str(dictOfMolecules[x].molecule_type)