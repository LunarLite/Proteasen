from .AminoAcid import Amino_acid
import sys

from Algorithms import random_algorithm
from random import randint
from Algorithms import breadth_algorithm
from Algorithms import hillclimber_algorithm

# imports required for plot
import matplotlib.pyplot as plt
import numpy as np

# setup for plot
fig = plt.figure()
fig.suptitle('AminoAcidChain')

# amino acid chain. 
class Amino_acid_chain:
	def __init__(self):
		self.chain = []

	def create(self, sequence):

		# iterate over each character in command line argument
		for c in sequence:

			# allow only H and P in command line argument.
			# set molecule type to either hydrophobic or polair, as H or P indicates
			if (c.upper() == 'H'):
				molecule_type = "hydrophobic"

			elif (c.upper() == 'P'):
				molecule_type = "polair"

			else: 
				sys.exit("Usage: application.py algorithm HHPHHHPHPHHHPH")

			# append amino acid with appropriate molecule type to chain
			self.chain.append(Amino_acid(molecule_type))

	# determines optimal aminoacid chain configuration
	def fold(self, algorithm): 

		if algorithm == "Random" or algorithm == "random":
			output = random_algorithm.fold(self.chain)

			# if chain stuck in conflict, set coordinates back and fold again
			if output == 1:
				for i in self.chain:
					i.coordinates = [0, 0]
				self.fold(algorithm)
		# ensure proper usage
		elif algorithm == "Breadth" or algorithm == "breadth":
			output = breadth_algorithm.fold(self.chain)
			self.chain = output

		elif algorithm == "Hillclimber" or algorithm == "hillclimber":
			output = hillclimber_algorithm.fold(self.chain)
			self.chain = output

		else: 
			sys.exit("Usage: application.py algorithm HHPHHHPHPHHHPH")
			

	# calculates chain stability score
	def stability(self):
		
		# initialize score variable
		score = 0
		# iterate over chain, keeping track of the count
		for count, j in enumerate(self.chain):

			# if current aminoacid is hydrophobic, check for neigbouring aminoacids
			if j.molecule_type == "hydrophobic":

				# loop through remaining acids to check coordinates and molecule type
				# skip one acid (count + 2), since next acid in the string does not count for score
				for k in range(count + 2, len(self.chain)):

					# calculate absolute difference in x- and y-coordinates 
					x_difference = abs(j.coordinates[0] - self.chain[k].coordinates[0])
					y_difference = abs(self.chain[k].coordinates[1] - j.coordinates[1])

					# if abs x- and y-difference is 1, acids are positioned next to eachother
					# if neighbouring acids are hydrophobic, increase score
					if self.chain[k].molecule_type == "hydrophobic" and x_difference + y_difference == 1:
						score -= 1
		
		return score

	# plots aminoacid chain configuration
	def plot(self):
		
		# Add new subplot
		subPlot = fig.add_subplot(111)
		# create empty lists to store x and y coordinates
		x = []
		y = []

		
		# iterate over each aminoacid 
		for i in range(0, len(self.chain)):

			# store x and y coordinates of current aminoacid
			x.append(self.chain[i].coordinates[0])
			y.append(self.chain[i].coordinates[1])
		
		# subplot backbone aminoacid chain
		subPlot.plot(x, y, 'k-')
		# set subplot ticks to the exact amount required
		subPlot.set_xticks(x, False)
		subPlot.set_yticks(y, False)

		# iterate over each aminoacid
		for i in range(0, len(self.chain)):
			
			# check for type of current aminoacid
			if self.chain[i].molecule_type == "hydrophobic": 

				# plot red dot at coordinates of hydrophobic aminoacid
				subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'ro')
				plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'ro')

			elif self.chain[i].molecule_type == "polair":  

				# plot blue dot at coordinates of polair aminoacid
				subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'bo')
				plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'bo')
		
		# draw a grid behind Subplot 
		subPlot.grid()

		# display pop-up window with plot
		plt.show()