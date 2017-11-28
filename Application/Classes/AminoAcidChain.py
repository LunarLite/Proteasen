from .AminoAcid import Amino_acid
import sys

from Algorithms import random_algorithm
from random import randint
from Algorithms import breadth_algorithm
from Algorithms import hillclimber_algorithm
from Dependencies import helpers

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
			output = helpers.fold_random(self.chain)
			self.chain = output

		# ensure proper usage
		elif algorithm == "Breadth" or algorithm == "breadth":
			breadth_algorithm.fold(self)

		elif algorithm == "Hillclimber" or algorithm == "hillclimber":
			hillclimber_algorithm.execute(self)
			#self.chain = output
			# self.rotate()

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

	def rotate(self):

		# create array to store coordinates after rotation
		rotated_coordinates = []

		# create array to store direction strings
		directions = []

		# iterate over coordinates to create direction strings
		for i in range(1, len(self.chain)):

			# assign coordinate changes to appropriate direction strings
			# DIT KLOPT NOG NIET, BEKIJKEN VANAF ORIENTATIE VAN PEPTIDE ZELF
			if self.chain[i].coordinates[0] < self.chain[i - 1].coordinates[0]:
				directions.append("left")
			if self.chain[i].coordinates[0] > self.chain[i - 1].coordinates[0]:
				directions.append("right")
			if self.chain[i].coordinates[1] < self.chain[i - 1].coordinates[1]:
				directions.append("down")
			if self.chain[i].coordinates[1] > self.chain[i - 1].coordinates[1]:
				directions.append("up")

		# array with different possible changes
		changes = ["right", "left", "up", "down"]

		# create random integer that decides which direction will be changed
		to_change = randint(0, len(directions) - 1)

		# create random int that decides which change will be applied
		change = randint(0, 3)

		# when these two directions are the same, choose new change to apply
		while changes[change] == directions[to_change]:
			change = randint(0, 3)

		print("changing number", to_change, "from", directions[to_change], "to", changes[change], "..")

		# execute the change
		directions[to_change] = changes[change]

		# iterate over coordinates before the change to store, they stay the same
		for i in range(0, to_change + 1):
			rotated_coordinates.append(self.chain[i].coordinates)

		# iterate over directions to determine new coordinates
		# DIT KLOPT NOG NIET, BEKIJKEN VANAF ORIENTATIE VAN PEPTIDE ZELF
		for i in range(to_change, len(directions)):
			if directions[i] == "right":
				rotated_coordinates.append([rotated_coordinates[i][0] + 1, rotated_coordinates[i][1]])
			if directions[i] == "left":
				rotated_coordinates.append([rotated_coordinates[i][0] - 1, rotated_coordinates[i][1]])
			if directions[i] == "up":
				rotated_coordinates.append([rotated_coordinates[i][0], rotated_coordinates[i][1] + 1])
			if directions[i] == "down":
				rotated_coordinates.append([rotated_coordinates[i][0], rotated_coordinates[i][1] - 1])
			
		return rotated_coordinates

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