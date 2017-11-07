
# Aminoacid. 
# Can be either hydrophobic or polair.
# Gets a position assigned based on the algorythm.
class Amino_acid:
	def __init__(self, molecule_type):
		self.molecule_type = molecule_type
		self.x = 0
		self.y = 0
