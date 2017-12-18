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
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import copy

# setup for plot
fig = plt.figure()

# amino acid chain. 
class Amino_acid_chain:
	"""Stores a chain of amino_acid objects which can then be manipulated by it's functions.
	
	Keyfuntions:
	__init__ -- creates a list and score variable for itself and calls the create()function.
	create() -- iterates through self.sequence and creates amino_acid's for each iteration.
	stability() -- determines the current chain's score.
	rotate() -- randomly rotates one amino_acid of self.chain
	plot() -- draws out a plot using the matplotlib library.
	drawLines2D -- draws lines on the plot, showing where points were scored (in 2D)
	drawLines3D -- draws lines on the plot, showing where points were scored (in 3D)
	
    """
	
	def __init__(self, sequence):
		"""Creates the neccesary variables for itself and stores the given sequence before creating itself.
		
		Keyword arguments:
		sequence -- A string containing a number of "P"/"H"/"C" 's
		
		"""
		self.chain = []
		self.score = 0
		self.sequence = sequence
		self.create()

	def create(self):
		"""This function appends Amino_acid objects with 
		molecule_type according to sequence to self.chain.
	
		Keyword arguments:
		sequence -- A string containing a number of "P"/"H"/"C" 's
		
		"""

		# iterate over each character in the sequence
		for c in self.sequence:

			# allow only P/H/C from sequence
			# set molecule type to either polair (P), hydrophobic (H) or cysteine (C)
			if (c.upper() == 'H'):
				molecule_type = "hydrophobic"

			elif (c.upper() == 'P'):
				molecule_type = "polair"

			elif (c.upper() == 'C'): 
				molecule_type = "cysteine"

			else: 
				# warn user if commandline arguement was wrong
				sys.exit("\nUsage: application.py dimension algorithm HHPHHHPHPHHHPH/CHPHCHPHCHHCPH\n"
					"dimension: 2D/3D\nalgorithms: Random / Breadth / Breadth_heur / Depth / Depth_hill / Hillclimber / Randomhillclimber / RandomSimulatedannealing\n")

			# append amino acid with appropriate molecule type to chain
			self.chain.append(Amino_acid(molecule_type))

	def stability(self): 
		"""This function calculates self.score, based on the 
		coordinates of the hydrophobic (and cysteine) Amino_acid objects in self.chain."""
	
		self.score = 0
		hydro_connections = 0
		cys_connections = 0
		hydro_cys_connections = 0

		# create arrays to remember coordinates of hydrophobic and cysteine aminoacids
		hydro_coordinates = []
		cys_coordinates = []

		# iterate over aminoacids in chain
		for i, aminoacid in enumerate(self.chain):

			# if the amino_acid is a hydrophobe:
			if(aminoacid.molecule_type == "hydrophobic"):

				# iterate over remembered hydrophobic coordinates
				for coordinate in hydro_coordinates:

					# count score -1 if current hydrophobic aminoacid neighbours a remembered hydrophobic aminoacid
					if abs(aminoacid.coordinates[0] - coordinate[0]) + abs(aminoacid.coordinates[1] - coordinate[1]) + abs(aminoacid.coordinates[2] - coordinate[2]) == 1:
						self.score -= 1

				# iterate over remembered cysteine coordinates
				for coordinate in cys_coordinates:

					# count score -1 if current cysteine aminoacid neighbours a remembered hydrophobic aminoacid
					if abs(aminoacid.coordinates[0] - coordinate[0]) + abs(aminoacid.coordinates[1] - coordinate[1]) + abs(aminoacid.coordinates[2] - coordinate[2]) == 1:
						self.score -= 1
						
				# remember current hydrophobic aminoacid
				hydro_coordinates.append(aminoacid.coordinates)

				# count connections between neigbouring hydrophobic aminoacids in chain and rebalance the score
				if i != len(self.chain)-1:
					if self.chain[i+1].molecule_type == "hydrophobic":
						hydro_connections += 1
					if self.chain[i+1].molecule_type == "cysteine":
						hydro_cys_connections += 1
						
			# if the amino_acid is a cysteine:
			if(aminoacid.molecule_type == "cysteine"):

				# iterate over remembered cysteine coordinates
				for coordinate in cys_coordinates:

					# count score -5 if current cysteine aminoacid neighbours a remembered cysteine aminoacid
					if abs(aminoacid.coordinates[0] - coordinate[0]) + abs(aminoacid.coordinates[1] - coordinate[1]) + abs(aminoacid.coordinates[2] - coordinate[2]) == 1:
						self.score -= 5

				# iterate over remembered hydrophobic coordinates
				for coordinate in hydro_coordinates:

					# count score -1 if current cysteine aminoacid neighbours a remembered hydrophobic aminoacid
					if abs(aminoacid.coordinates[0] - coordinate[0]) + abs(aminoacid.coordinates[1] - coordinate[1]) + abs(aminoacid.coordinates[2] - coordinate[2]) == 1:
						self.score -= 1
	
				# remember current cysteine aminoacid
				cys_coordinates.append(aminoacid.coordinates)

				# count connections between neigbouring cysteine aminoacids in chain and rebalance the score
				if i != len(self.chain)-1:
					if self.chain[i+1].molecule_type == "cysteine":
						cys_connections += 1
					if self.chain[i+1].molecule_type == "hydrophobic":
						hydro_cys_connections += 1

		# revise score taking into account connections between hydrofobic aminoacids and between cysteine aminoacids in chain
		self.score += hydro_connections
		self.score += cys_connections * 5 
		self.score += hydro_cys_connections
		
	def rotate(self, dimension, errors):
		"""This function returns a copy of self.chain 
		with one random Amino_acid rotated.
		
		Keyword arguments:
		dimension -- determines wether the rotation occurs in 2D or 3D
		errors -- the amount of errors while rotating.
		"""

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

		# determine dimension
		if dimension == "3d":
			changes.append("out")
			changes.append("in")

		# create random integer that decides which direction will be changed
		to_change = randint(0, len(abs_directions) - 1)

		# create random int that decides which change will be applied
		change = randint(0, len(changes) - 1)

		# when these two directions are the same, choose new change to apply
		while changes[change] == abs_directions[to_change]:
			change = randint(0, len(changes) - 1)


		# execute the change
		abs_directions[to_change] = changes[change]

		# iterate over coordinates before the change to store, they stay the same
		for i in range(0, to_change + 1):
			rotated_coordinates.append(self.chain[i].coordinates)

		doubles = 0

		# iterate over directions to determine new coordinates whilst checking overlaps
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

		# if the amount of errors made is bigger than 50, quit and return error.
		if errors > 50:
			return 1
		elif doubles != 0:
			
			# try to fold again, remembering errors made 
			new_chain = self.rotate(dimension, errors)

		return new_chain

	def plot(self, dimension):
		"""This function plots self.chain, based on the coordinates 
		of the Amino_acids in self.chain
		
		Keyword arguments:
		dimension -- determines wether the plot will be created/filled in 2D or 3D
		"""
		
		# set the title for the figure
		fig.suptitle("AminoAcidChain \n Score: " + str(self.score))
		if (dimension == "2d"):
		
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
					subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], "ro")
					plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], "ro")

				elif self.chain[i].molecule_type == "polair":  
					# plot blue dot at coordinates of polair aminoacid
					subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], "bo")
					plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], "bo")

				elif self.chain[i].molecule_type =="cysteine":
					# plot green dot at coordinates of cysteine aminoacid
					subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], "go")
					plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], "go")

			self.drawLines2D(subPlot)
			# draw a grid behind Subplot 
			subPlot.grid()
			# display pop-up window with plot
			plt.show()
			
		else:
			# Add new 3D subplot
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
			hydrophobes = []
			cysteines = []
			# iterate over each aminoacid and add them to plot
			for i in range(0, len(self.chain)):
				# fetch required coordinates
				xs = self.chain[i].coordinates[0]
				ys = self.chain[i].coordinates[1]
				zs = self.chain[i].coordinates[2]
				# check for type of current aminoacid and change colour accordingly
				if self.chain[i].molecule_type == "hydrophobic": 
					c = 'r'
					# store hydrophobe position
					hydrophobes.append([self.chain[i].coordinates[0], self.chain[i].coordinates[1], self.chain[i].coordinates[2]])
				elif self.chain[i].molecule_type == "polair":  
					c = 'b'
				elif self.chain[i].molecule_type =="cysteine":
					c = 'g'
					# store cysteine position
					cysteines.append([self.chain[i].coordinates[0], self.chain[i].coordinates[1], self.chain[i].coordinates[2]])
				# draw amino_acid
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
			
			# draw coloured lines for the scores
			self.drawLines3D(subPlot)
			# draw a grid behind Subplot 
			subPlot.grid()
			# display pop-up window with plot
			plt.show()
		
	def drawLines3D(self, subPlot): 
		"""This function draws extra lines between all point-scoring nodes in 3D.
		
		Keyword arguments:
		subPlot -- The actual plot on which the drawing occurs.
		"""
	
		# iterate over chain, keeping track of the count and indexed item
		for count, j in enumerate(self.chain):
			# if current aminoacid is hydrophobic, check for neigbouring aminoacids
			if j.molecule_type == "hydrophobic":
				# loop through remaining acids to check coordinates and molecule type
				# skip one acid (count + 2), since next acid in the string does not count for score
				for k in range(count + 3, len(self.chain)):
					# calculate absolute difference in x- and y-coordinates 
					x_difference = abs(j.coordinates[0] - self.chain[k].coordinates[0])
					y_difference = abs(j.coordinates[1] - self.chain[k].coordinates[1])
					z_difference = abs(j.coordinates[2] - self.chain[k].coordinates[2])
					# if abs x- and y-difference is 1, acids are positioned next to eachother
					# if neighbouring acids are hydrophobic, increase score
					if self.chain[k].molecule_type == "hydrophobic" and x_difference + y_difference + z_difference == 1:
						subPlot.plot([j.coordinates[0], self.chain[k].coordinates[0]], [j.coordinates[1], self.chain[k].coordinates[1]], [j.coordinates[2], self.chain[k].coordinates[2]], 'r:')
					if self.chain[k].molecule_type == "cysteine" and x_difference + y_difference + z_difference == 1:
						subPlot.plot([j.coordinates[0], self.chain[k].coordinates[0]], [j.coordinates[1], self.chain[k].coordinates[1]], [j.coordinates[2], self.chain[k].coordinates[2]], 'r--')
			# if current aminoacid is a cysteine, check for neigbouring aminoacids
			if j.molecule_type == "cysteine":
				# loop through remaining acids to check coordinates and molecule type
				# skip one acid (count + 2), since next acid in the string does not count for score
				for k in range(count + 3, len(self.chain)):
					# calculate absolute difference in x- and y-coordinates 
					x_difference = abs(j.coordinates[0] - self.chain[k].coordinates[0])
					y_difference = abs(j.coordinates[1] - self.chain[k].coordinates[1])
					z_difference = abs(j.coordinates[2] - self.chain[k].coordinates[2])
					# if abs x- and y-difference is 1, acids are positioned next to eachother
					# if neighbouring acids are hydrophobic, increase score
					if self.chain[k].molecule_type == "cysteine" and x_difference + y_difference + z_difference == 1:
						subPlot.plot([j.coordinates[0], self.chain[k].coordinates[0]], [j.coordinates[1], self.chain[k].coordinates[1]], [j.coordinates[2], self.chain[k].coordinates[2]], 'g:')
					if self.chain[k].molecule_type == "hydrophobic" and x_difference + y_difference + z_difference == 1:
						subPlot.plot([j.coordinates[0], self.chain[k].coordinates[0]], [j.coordinates[1], self.chain[k].coordinates[1]], [j.coordinates[2], self.chain[k].coordinates[2]], 'r--')
						
	def drawLines2D(self, subPlot): 
		"""This function draws extra lines between all point-scoring nodes in 3D.
		
		Keyword arguments:
		subPlot -- The actual plot on which the drawing occurs.
		"""
		
		# iterate over chain, keeping track of the count and indexed item
		for count, j in enumerate(self.chain):
			# if current aminoacid is hydrophobic, check for neigbouring aminoacids
			if j.molecule_type == "hydrophobic":
				# loop through remaining acids to check coordinates and molecule type
				# skip one acid (count + 2), since next acid in the string does not count for score
				for k in range(count + 3, len(self.chain)):
					# calculate absolute difference in x- and y-coordinates 
					x_difference = abs(j.coordinates[0] - self.chain[k].coordinates[0])
					y_difference = abs(j.coordinates[1] - self.chain[k].coordinates[1])
					# if abs x- and y-difference is 1, acids are positioned next to eachother
					# if neighbouring acids are hydrophobic, increase score
					if self.chain[k].molecule_type == "hydrophobic" and x_difference + y_difference == 1:
						subPlot.plot([j.coordinates[0], self.chain[k].coordinates[0]], [j.coordinates[1], self.chain[k].coordinates[1]], 'r:')
					if self.chain[k].molecule_type == "cysteine" and x_difference + y_difference == 1:
						subPlot.plot([j.coordinates[0], self.chain[k].coordinates[0]], [j.coordinates[1], self.chain[k].coordinates[1]], 'r--')
			# if current aminoacid is a cysteine, check for neigbouring aminoacids
			if j.molecule_type == "cysteine":
				# loop through remaining acids to check coordinates and molecule type
				# skip one acid (count + 2), since next acid in the string does not count for score
				for k in range(count + 3, len(self.chain)):
					# calculate absolute difference in x- and y-coordinates 
					x_difference = abs(j.coordinates[0] - self.chain[k].coordinates[0])
					y_difference = abs(j.coordinates[1] - self.chain[k].coordinates[1])
					# if abs x- and y-difference is 1, acids are positioned next to eachother
					# if neighbouring acids are hydrophobic, increase score
					if self.chain[k].molecule_type == "cysteine" and x_difference + y_difference == 1:
						subPlot.plot([j.coordinates[0], self.chain[k].coordinates[0]], [j.coordinates[1], self.chain[k].coordinates[1]], 'g:')
					if self.chain[k].molecule_type == "hydrophobic" and x_difference + y_difference == 1:
						subPlot.plot([j.coordinates[0], self.chain[k].coordinates[0]], [j.coordinates[1], self.chain[k].coordinates[1]], 'r--')
