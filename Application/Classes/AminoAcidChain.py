# AminoAcidChain.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the Amino_acid_chain class.

import timeit
import sys
from random import randint

from .AminoAcid import Amino_acid
from Dependencies import helpers

# imports required for plot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import copy

# setup for plot
fig = plt.figure()

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
			elif (c.upper() == 'C'): 
				molecule_type = "cysteine"

			else: 
				sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Hillclimber / Randomhillclimber\n")

			# append amino acid with appropriate molecule type to chain
			self.chain.append(Amino_acid(molecule_type))


	# calculates chain stability score
	def stability(self): 
		"""This function calculates self.score, based on the 
		coordinates of the hydrophobic (and cysteine) Amino_acid objects in self.chain."""
		
		self.score = 0
		hydro_connections = 0
		cys_connections = 0

		# create arrays to remember coordinates of hydrophobic and cysteine aminoacids
		hydro_coordinates = []
		cys_coordinates = []


		# iterate over aminoacids in chain
		for i, aminoacid in enumerate(self.chain):

			if(aminoacid.molecule_type == "hydrophobic"):

				# iterate over remembered hydrophobic coordinates
				for coordinate in hydro_coordinates:

					# count score -1 if current hydrophobic aminoacid neighbours a remembered hydrophobic aminoacid
					if abs(aminoacid.coordinates[0] - coordinate[0]) + abs(aminoacid.coordinates[1] - coordinate[1]) + abs(aminoacid.coordinates[2] - coordinate[2]) == 1:
						self.score -= 1

				# remember current hydrophobic aminoacid
				hydro_coordinates.append(aminoacid.coordinates)

				# count connections between neigbouring hydrophobic aminoacids in chain
				if i != len(self.chain)-1:
					if self.chain[i+1].molecule_type == "hydrophobic":
						hydro_connections += 1

			if(aminoacid.molecule_type == "cysteine"):

				# iterate over remembered cysteine coordinates
				for coordinate in cys_coordinates:

					# count score -5 if current cysteine aminoacid neighbours a remembered cysteine aminoacid
					if abs(aminoacid.coordinates[0] - coordinate[0]) + abs(aminoacid.coordinates[1] - coordinate[1]) + abs(aminoacid.coordinates[2] - coordinate[2]) == 1:
						self.score -= 5

				# remember current cysteine aminoacid
				cys_coordinates.append(aminoacid.coordinates)

				# count connections between neigbouring cysteine aminoacids in chain
				if i != len(self.chain)-1:
					if self.chain[i+1].molecule_type == "cysteine":
						cys_connections += 1

		# revise score taking into account connections between hydrofobic aminoacids and between cysteine aminoacids in chain
		self.score += hydro_connections
		self.score += cys_connections * 5 

	def rotate(self, dimension, errors):
		"""This function returns a copy of self.chain 
		with one random Amino_acid rotated."""

		# create array to store coordinates after rotation
		rotated_coordinates = []

		# create array to store absolute direction strings of previous step
		abs_directions = []

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
			if self.chain[i].coordinates[2] < self.chain[i - 1].coordinates[2]:
				abs_directions.append("out")
			if self.chain[i].coordinates[2] > self.chain[i - 1].coordinates[2]:
				abs_directions.append("in")

		

		# array with different possible changes
		changes = ["right", "left", "up", "down"]

		if dimension == "3d" or dimension == "3D":
			changes.append("out")
			changes.append("in")

		# create random integer that decides which direction will be changed
		to_change = randint(0, len(abs_directions) - 1)

		# create random int that decides which change will be applied
		change = randint(0, len(changes) - 1)

		# when these two directions are the same, choose new change to apply
		while changes[change] == abs_directions[to_change]:
			change = randint(0, len(changes) - 1)

		# print("changing number", to_change, "from", abs_directions[to_change], "to", changes[change], "..")

		# execute the change
		abs_directions[to_change] = changes[change]

		# iterate over coordinates before the change to store, they stay the same
		for i in range(0, to_change + 1):
			rotated_coordinates.append(self.chain[i].coordinates)

		doubles = 0

		# iterate over directions to determine new coordinates
		for i in range(to_change, len(abs_directions)):
			if abs_directions[i] == "right":
				new_coordinates = [rotated_coordinates[i][0] + 1, rotated_coordinates[i][1], rotated_coordinates[i][2]]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates
			if abs_directions[i] == "left":
				new_coordinates = [rotated_coordinates[i][0] - 1, rotated_coordinates[i][1], rotated_coordinates[i][2]]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates
			if abs_directions[i] == "up":
				new_coordinates = [rotated_coordinates[i][0], rotated_coordinates[i][1] + 1, rotated_coordinates[i][2]]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates
			if abs_directions[i] == "down":
				new_coordinates = [rotated_coordinates[i][0], rotated_coordinates[i][1] - 1, rotated_coordinates[i][2]]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates
			if abs_directions[i] == "out":
				new_coordinates = [rotated_coordinates[i][0], rotated_coordinates[i][1], rotated_coordinates[i][2] + 1]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates
			if abs_directions[i] == "in":
				new_coordinates = [rotated_coordinates[i][0], rotated_coordinates[i][1], rotated_coordinates[i][2] - 1]
				if new_coordinates in rotated_coordinates:
					doubles = 1
					errors += 1
					break;
				rotated_coordinates.append(new_coordinates)
				new_chain[i + 1].coordinates = new_coordinates

		if errors > 50:
			return 1
		elif doubles != 0:
			new_chain = self.rotate(dimension, errors)

		return new_chain

	

	# plots aminoacid chain configuration
	def plot(self, dimension):
		fig.suptitle("AminoAcidChain \n Score: " + str(self.score))
		"""This function plots self.chain, based on the coordinates 
		of the Amino_acids in self.chain"""
		
		# Add new subplot
		subPlot = fig.add_subplot(111, projection='3d')

		# create empty lists to store x and y coordinates
		x = []
		y = []
		z = []
		
		# iterate over each aminoacid 
		for i in range(0, len(self.chain)):
			# store x and y coordinates of current aminoacid
			x.append(self.chain[i].coordinates[0])
			y.append(self.chain[i].coordinates[1])
			z.append(self.chain[i].coordinates[2])
		# subplot backbone aminoacid chain
		subPlot.plot(x, y, z, 'k-')	
		# iterate over each aminoacid and add them to plot
		for i in range(0, len(self.chain)):
			
			xs = self.chain[i].coordinates[0]
			ys = self.chain[i].coordinates[1]
			zs = self.chain[i].coordinates[2]
			
			# check for type of current aminoacid
			if self.chain[i].molecule_type == "hydrophobic": 
				c = 'r'
			elif self.chain[i].molecule_type == "polair":  
				c = 'b'
			elif self.chain[i].molecule_type =="cysteine":
				c = 'g'
			subPlot.scatter(xs, ys, zs, c=c, marker='o')
		# determine the ranges
		maxes = [max(x), max(y), max(z)]
		mins = [min(x), min(y), min(z)]
		maxlim = max(maxes)
		minlim = min(mins)
		# set the ranges
		subPlot.set_xlim([minlim,maxlim])
		subPlot.set_ylim([minlim,maxlim])
		subPlot.set_zlim([minlim,maxlim])
		# disable decimals
		subPlot.set_xticks(x, False)
		subPlot.set_yticks(y, False)
		subPlot.set_zticks(z, False)
		# add labels
		subPlot.set_xlabel('X-axis')
		subPlot.set_ylabel('Y-axis')
		subPlot.set_zlabel('Z-axis')
		# draw a grid behind Subplot 
		subPlot.grid()
		# display pop-up window with plot
		plt.show()

