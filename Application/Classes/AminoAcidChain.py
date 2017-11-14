import AminoAcid
import sys

from Dependencies import helpers
from random import randint

# Imports required for plot
import matplotlib.pyplot as plt
import numpy as np
# Setup for plot
fig = plt.figure()
fig.suptitle('AminoAcidChain')

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
		
		subPlot = fig.add_subplot(111)
		# Create empty lists to store x and y coordinates.
		x = []
		y = []

		
		# Iterate over each aminoacid. 
		for i in range(0, len(self.chain)):

			# Store x and y coordinates of current aminoacid.
			x.append(self.chain[i].coordinates[0])
			y.append(self.chain[i].coordinates[1])
		
		# Plot backbone aminoacid chain.
		subPlot.plot(x, y, 'k-')
		subPlot.set_xticks(x, False)
		subPlot.set_yticks(y, False)

		# Iterate over each aminoacid.
		for i in range(0, len(self.chain)):
			
			# Check for type of current aminoacid. 
			if self.chain[i].molecule_type == "hydrophobic": 

				# Plot red dot at coordinates of hydrophobic aminoacid.
<<<<<<< HEAD
				subPlot.plot(self.chain[i].x, self.chain[i].y, 'ro')
=======
				plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'ro')
>>>>>>> ed7c541e6732cefc37959b567691fd203a53cbad

			elif self.chain[i].molecule_type == "polair":  

				# Plot blue dot at coordinates of polair aminoacid.
<<<<<<< HEAD
				subPlot.plot(self.chain[i].x, self.chain[i].y, 'bo')
=======
				plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'bo')
>>>>>>> ed7c541e6732cefc37959b567691fd203a53cbad
		
		# Draw a grid behind plots. 
		subPlot.grid()

		# Display pop-up window with plot. 
		plt.show()
		


