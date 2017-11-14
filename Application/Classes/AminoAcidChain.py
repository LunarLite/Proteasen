import AminoAcid
import sys

from Dependencies import helpers
from random import randint
from matplotlib import pyplot as plt

# Amino acid chain. 
class Amino_acid_chain:
	def __init__(self):
		self.chain = []

	def create(self, chain_prototype):

		# Iterate over each character in command line argument. 
		for c in chain_prototype:

			# Allow only H and P in command line argument. 
			# Set molecule type to either hydrophobic or polair, as H or P indicates.
			if (c.upper() == 'H'):
				molecule_type = "hydrophobic"

			elif (c.upper() == 'P'):
				molecule_type = "polair"

			else: 
				sys.exit("Usage: python program.py algorithm HPPHHPPHH")

			# Append amino acid with appropriate molecule type to chain.
			self.chain.append(AminoAcid.Amino_acid(molecule_type))

	# Determines optimal aminoacid chain configuration.
	def fold(self, algorithm): 

		if algorithm == "Random" or algorithm == "random":
			helpers.random(self.chain)
			
		# ensure proper usage
		else: 
			sys.exit("Usage: python program.py algorithm HPPHHPPHH")

	# Plots aminoacid chain configuration.
	def plot(self):
		
		# Create empty lists to store x and y coordinates.
		x = []
		y = []

		# Iterate over each aminoacid. 
		for i in range(0, len(self.chain)):

			# Store x and y coordinates of current aminoacid.
			x.append(self.chain[i].coordinates[0])
			y.append(self.chain[i].coordinates[1])
		
		# Plot backbone aminoacid chain.
		plt.plot(x, y, 'k-')

		# Iterate over each aminoacid.
		for i in range(0, len(self.chain)):
			
			# Check for type of current aminoacid. 
			if self.chain[i].molecule_type == "hydrophobic": 

				# Plot red dot at coordinates of hydrophobic aminoacid.
				plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'ro')

			elif self.chain[i].molecule_type == "polair":  

				# Plot blue dot at coordinates of polair aminoacid.
				plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'bo')
		
		# Draw a grid behind plots. 
		plt.grid()

		# Display pop-up window with plot. 
		plt.show()
		


