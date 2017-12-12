# AminoAcid.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the Amino_acid class.
#
# Can be either hydrophobic or polair.
# Gets a position (coordinates) assigned based on the algorythm.


class Amino_acid:
	def __init__(self, molecule_type):
		self.molecule_type = molecule_type
		# [x, y, z]
		self.coordinates = [0, 0, 0]

