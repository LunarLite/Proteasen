import AminoAcid
import sys

from Algorithms import Random
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
			Random.fold(self.chain)
			
		# ensure proper usage
		else: 
			sys.exit("Usage: python program.py algorithm HPPHHPPHH")

	# Plots aminoacid chain configuration.
	def plot(self):
		
		# Add new subplot
		subPlot = fig.add_subplot(111)
		# Create empty lists to store x and y coordinates.
		x = []
		y = []

		
		# Iterate over each aminoacid. 
		for i in range(0, len(self.chain)):

			# Store x and y coordinates of current aminoacid.
			x.append(self.chain[i].coordinates[0])
			y.append(self.chain[i].coordinates[1])
		
		# Subplot backbone aminoacid chain.
		subPlot.plot(x, y, 'k-')
		# Set subplot ticks to the exact amount required
		subPlot.set_xticks(x, False)
		subPlot.set_yticks(y, False)

		# Iterate over each aminoacid.
		for i in range(0, len(self.chain)):
			
			# Check for type of current aminoacid. 
			if self.chain[i].molecule_type == "hydrophobic": 

				# Plot red dot at coordinates of hydrophobic aminoacid.
				subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'ro')
				plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'ro')

			elif self.chain[i].molecule_type == "polair":  

				# Plot blue dot at coordinates of polair aminoacid.
				subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'bo')
				plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'bo')
		
		# Draw a grid behind Subplot 
		subPlot.grid()

		# Display pop-up window with plot
		plt.show()