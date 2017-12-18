# simulated_annealing.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the simulated annealing algorithm
# can have either a "straight_folded" or "random_folded" 
# amino acid chain as starting point. Dimension can either be 2D or 3D
# 
# Able to fold amino acid chains consisting of > 50 amino acids (H / P / C +  2D and 3D)
# --> all of the H/P chains and H/P/C chains
#

from Algorithms import random_algorithm
from Classes import AminoAcidChain
import copy
from Dependencies import helpers
from random import randint, random

import math

def execute(input_chain, start_point, iterations, dimension):
	""" Folds using simulated annealing, keeping chains only with a probability
	derived from exponential cooling schedule.

	Keyword arguments:
	input_chain -- the chain to work with (contains acid type and coordinates, [x, y, c]
	start_point -- the chain position with which to start making changes 
		(straight-folded / random_folded)
	iterations -- the amount of changes this function will make (10000 recommended)
	dimension -- the dimension to fold chain in (2D / 3D)"""


    # parameters simulated annealing  
	T_begin = 100
	T_current = 0
	T_end = 1
	

	# initialize variables to store temporary acid chains
	new_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	rotated_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	best_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)\


	if start_point == "straight_folded":

		# fold amino acid chain straight
		for i, acid in enumerate(new_acid_chain.chain):
			acid.coordinates = [i, 0, 0]
	
	elif start_point == "random_folded":
		new_acid_chain = helpers.fold_random(input_chain, dimension)

	
	new_acid_chain.stability()
	start_score = new_acid_chain.score

	current_iteration = 0

	while current_iteration < iterations:

		# calculate current temperature using exponential cooling schedule
		T_current = T_begin * (T_end / T_begin) ** ((current_iteration * 1.5 ) / iterations)
	
		rotated_chain = new_acid_chain.rotate(dimension, 0)
		if rotated_chain == 1:	
			# no possible rotations found, break out of loop
			break

		# set chain to new rotated_chain and update stability score
		rotated_acid_chain.chain = rotated_chain
		rotated_acid_chain.stability()


		cost = ((new_acid_chain.score) - rotated_acid_chain.score)
		acceptance_prob = math.e ** (cost / T_current)

		if random() < acceptance_prob: 
			# set current chain to new chain and update stability score
			new_acid_chain.chain = rotated_chain
			new_acid_chain.stability()

		if acceptance_prob == 1: 
			if random() < 0.5: 
				# set current chain to new chain and update stability score
				new_acid_chain.chain = rotated_chain 
				new_acid_chain.stability()

		# increase number of iterations with 1
		current_iteration += 1


	# print start_score to show whether hillclimber improved stability
	print("Start score:", start_score)

	# set input chain random folded chain with best score
	input_chain.chain = new_acid_chain.chain








