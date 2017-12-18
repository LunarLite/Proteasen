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

def execute(input_chain, start_point, total_iterations, dimension):
	""" Folds using simulated annealing, keeping chains only with a probability of exponential cooling schedule.

	Keyword arguments:
	input_chain -- the chain to work with (contains acid type and coordinates, [x, y, c]
	start_point -- the chain position with which to start making changes (straight-folded / random_folded)
	iterations -- the amount of changes this function will make (10000 recommended)
	dimension -- the dimension to fold chain in (2D / 3D)"""


    # parameters simulated annealing  
	annealing_type = "Exponential"
	T_begin = 30000
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
			# print(new_acid_chain.chain[i].coordinates)
	
	elif start_point == "random_folded":
		new_acid_chain = helpers.fold_random(input_chain, dimension)

	
	new_acid_chain.stability()
	start_score = new_acid_chain.score
	# print("stability now: ", start_score)

	current_iteration = 0

	while current_iteration < total_iterations:

		if annealing_type == "Lineair":
			T_current = T_begin - current_iteration * (T_begin - T_end) / total_iterations

		elif annealing_type == "Exponential": 
			T_current = T_begin * math.pow((T_end / T_begin), ((current_iteration * 1.5 ) / total_iterations))
	

		rotated_chain = new_acid_chain.rotate(dimension, 0)
		if rotated_chain == 1:
			# print("no possible rotations found at attempt nr", current_iteration)
			
			# no possible rotations found, break out of loop
			break

		# set chain to new rotated_chain and update stability score
		rotated_acid_chain.chain = rotated_chain
		rotated_acid_chain.stability()


		cost = ((new_acid_chain.score) - rotated_acid_chain.score)
		acceptance_prob = math.pow(math.e, (cost / T_current))

		# print("new", rotated_acid_chain.score)
		# print("prev", new_acid_chain.score)
		# print("cost", cost)
		# print("prob", acceptance_prob)
		if random() < acceptance_prob: 
			# print("get in")

			# set current chain to new chain and update stability score
			new_acid_chain.chain = rotated_chain
			new_acid_chain.stability()

		if acceptance_prob == 1: 
			if random() < 0.5: 
				# set current chain to new chain and update stability score
				new_acid_chain.chain = rotated_chain 
				new_acid_chain.stability()

		# increase number of attempts with 1
		current_iteration += 1


	# print start_score to show whether hillclimber improved stability
	print("Start score:", start_score)

	# set input chain random folded chain with best score
	input_chain.chain = new_acid_chain.chain








