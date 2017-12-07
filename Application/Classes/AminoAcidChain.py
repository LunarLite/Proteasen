import timeit
import sys
from random import randint

from .AminoAcid import Amino_acid
from Dependencies import helpers

# imports required for plot
import matplotlib.pyplot as plt
import numpy as np
import copy

# setup for plot
fig = plt.figure()
fig.suptitle('AminoAcidChain')

# amino acid chain. 
class Amino_acid_chain:
	def __init__(self, sequence):
		self.chain = []
		self.score = 0
		self.sequence = sequence
		self.create()

	def create(self):
		"""This function appends Amino_acid objects with 
		molecule_type according to sequence to self.chain."""

		# iterate over each character in command line argument
		for c in self.sequence:

			# allow only H and P in command line argument.
			# set molecule type to either hydrophobic or polair, as H or P indicates
			if (c.upper() == 'H'):
				molecule_type = "hydrophobic"

			elif (c.upper() == 'P'):
				molecule_type = "polair"

			else: 
				sys.exit("\nUsage: application.py algorithm HHPHHHPHPHHHPH\n"
					"algorithms: Random/Breadth/Breadth_heur/Hillclimber/Randomhillclimber\n")

			# append amino acid with appropriate molecule type to chain
			self.chain.append(Amino_acid(molecule_type))



	# # calculates chain stability score
	# def stability(self):

	# 	start = timeit.default_timer()
	# 	# initialize score variable
	# 	score = 0
	# 	# iterate over chain, keeping track of the count
	# 	for count, j in enumerate(self.chain):

	# 		# if current aminoacid is hydrophobic, check for neigbouring aminoacids
	# 		if j.molecule_type == "hydrophobic":

	# 			# loop through remaining acids to check coordinates and molecule type
	# 			# skip one acid (count + 2), since next acid in the string does not count for score
	# 			for k in range(count + 2, len(self.chain)):

	# 				# calculate absolute difference in x- and y-coordinates 
	# 				x_difference = abs(j.coordinates[0] - self.chain[k].coordinates[0])
	# 				y_difference = abs(self.chain[k].coordinates[1] - j.coordinates[1])

	# 				# if abs x- and y-difference is 1, acids are positioned next to eachother
	# 				# if neighbouring acids are hydrophobic, increase score
	# 				if self.chain[k].molecule_type == "hydrophobic" and x_difference + y_difference == 1:
	# 					score -= 1

	# 	stop = timeit.default_timer()
	# 	print("Runtimeeee:", (stop - start))
	# 	print("hoi")
		
	# 	return score


	# calculates chain stability score
	def stability(self): 
		"""This function calculates self.score, based on the 
		coordinates of the hydrophobic Amino_acid objects in self.chain."""
		
		self.score = 0
		hydro_connenctions = 0

		# create array to remember coordinates of hydrophobic aminoacids
		hydro_coordinates = []

		# iterate over aminoacids in chain
		for i, aminoacid in enumerate(self.chain):

			if(aminoacid.molecule_type == "hydrophobic"):

				# iterate over remembered hydrophobic coordinates
				for coordinate in hydro_coordinates:

					# count score -1 if current hydrophobic aminoacid neighbours a remembered hydrophobic aminoacid
					if abs(aminoacid.coordinates[0] - coordinate[0]) + abs(aminoacid.coordinates[1] - coordinate[1]) == 1:
						self.score -= 1

				# remember current hydrophobic aminoacid
				hydro_coordinates.append(aminoacid.coordinates)

				# count connections between neigbouring hydrophobic aminoacids in chain
				if i != len(self.chain)-1:
					if self.chain[i+1].molecule_type == "hydrophobic":
						hydro_connenctions += 1

		# revise score taking into account connections between hydrofobic aminoacids in chain
		self.score += hydro_connenctions

	def rotate(self, errors):
		"""This function returns a copy of self.chain 
		with one random Amino_acid rotated."""

		# create array to store coordinates after rotation
		rotated_coordinates = []

		# create array to store absolute direction strings of previous step
		abs_directions = []

		# create array to store relative direction strings of current step
		directions = []

		# deepcopy is needed
		new_chain = copy.deepcopy(self.chain)

		# iterate over coordinates to create direction strings
		for i in range(1, len(self.chain)):

			# assign coordinate changes to absolute direction strings
			if self.chain[i].coordinates[0] < self.chain[i - 1].coordinates[0]:
				abs_directions.append("left")
			if self.chain[i].coordinates[0] > self.chain[i - 1].coordinates[0]:
				abs_directions.append("right")
			if self.chain[i].coordinates[1] < self.chain[i - 1].coordinates[1]:
				abs_directions.append("down")
			if self.chain[i].coordinates[1] > self.chain[i - 1].coordinates[1]:
				abs_directions.append("up")

		# array with different possible changes
		changes = ["right", "left", "up", "down"]

		# create random integer that decides which direction will be changed
		to_change = randint(0, len(abs_directions) - 1)

		# create random int that decides which change will be applied
		change = randint(0, len(changes) - 1)

		# when these two directions are the same, choose new change to apply
		while changes[change] == abs_directions[to_change]:
			change = randint(0, 3)

		# print("changing number", to_change, "from", abs_directions[to_change], "to", changes[change], "..")

		# execute the change
		abs_directions[to_change] = changes[change]

		# iterate over coordinates before the change to store, they stay the same
		for i in range(0, to_change + 1):
			rotated_coordinates.append(self.chain[i].coordinates[:])

		seen = []
		doubles = 0

		# print("NIEUWE COORDINATEN BEPALEN.....")
		# iterate over directions to determine new coordinates
		for i in range(to_change, len(abs_directions)):
			if abs_directions[i] == "right":
				new_coordinates = [rotated_coordinates[i][0] + 1, rotated_coordinates[i][1]]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates
				# print(i, new_coordinates)
			if abs_directions[i] == "left":
				new_coordinates = [rotated_coordinates[i][0] - 1, rotated_coordinates[i][1]]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates
				# print(i, new_coordinates)
			if abs_directions[i] == "up":
				new_coordinates = [rotated_coordinates[i][0], rotated_coordinates[i][1] + 1]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates
				# print(i, new_coordinates)
			if abs_directions[i] == "down":
				new_coordinates = [rotated_coordinates[i][0], rotated_coordinates[i][1] - 1]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates

		if errors > 50:
			return 1
		elif doubles != 0:
			new_chain = self.rotate(errors)

		return new_chain

	# plots aminoacid chain configuration
	def plot(self):
		"""This function plots self.chain, based on the coordinates 
		of the Amino_acids in self.chain"""
		
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