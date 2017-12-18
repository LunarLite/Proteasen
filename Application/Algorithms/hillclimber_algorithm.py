# hillclimber_algorithm.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the hillclimber algorithm
# can have either a "straight_folded", "random_folded" or "dept_chain"
# amino acid chain as starting point
# 
# Able to fold amino acid chains consisting of > 49 amino acids (H / P / C)
#
# 


from Algorithms import random_algorithm
from Classes import AminoAcidChain
import copy
from Dependencies import helpers


def execute(input_chain, start_point, iterations, dimension):
	"""Folds using hillclimber, keeping new chains only if score is equal or better than old chain.

	Keyword arguments:
	input_chain -- the chain to work with (contains acid type and coordinates, [x, y, z])
	start_point -- the chain position with which to start making changes (straight-folded / random-folded / after depth-first) 
	iterations -- the amount of changes this function will make (1000 recommended)
	dimension -- the dimension to fold chain in (2D / 3D)"""

	# initialize variables to store temporary acid chains
	new_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	rotated_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	best_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)

	# fold new_acid_chain accordinly based on input (start_point)
	if start_point == "straight_folded":

		# fold amino acid chain straight
		for i, acid in enumerate(new_acid_chain.chain):
			acid.coordinates = [i, 0, 0]
	
	elif start_point == "random_folded":

		# fold amino acid chain randomly
		new_acid_chain = helpers.fold_random(input_chain, dimension)

	elif start_point == "dept_chain":

		# set new amino acid chain to input_chainm (depth-first output)
		new_acid_chain = copy.deepcopy(input_chain)

	scores = []

	current_iteration = 0

	# score of current new_acid_chain is the start score
	new_acid_chain.stability()
	start_score = new_acid_chain.score

	# append current 
	# scores.append([current_iteration, start_score])

	while current_iteration < iterations:
		rotated_chain = new_acid_chain.rotate(dimension, 0)
		if rotated_chain == 1:
			print("no possible rotations found at iteration nr", current_iteration)
			
			# no possible rotations found, break out of loop
			break

		# set chain to new rotated_chain and update stability score
		rotated_acid_chain.chain = rotated_chain
		rotated_acid_chain.stability()

		# if new score is lower than current score
		if rotated_acid_chain.score <= new_acid_chain.score:

			# set current chain to new chain and update stability score
			new_acid_chain.chain = rotated_chain
			new_acid_chain.stability()

			# increase number of current_iteration with 1
			current_iteration += 1
		else: 

			# else, increase number of current_iteration with 1
			current_iteration += 1

		# scores.append([current_iteration, new_acid_chain.score])
	
	# print start_score to show whether hillclimber improved stability
	print("Start score:", start_score)
	
	# set input chain random folded chain with best score
	input_chain.chain = new_acid_chain.chain



	# with open("straight_hill_exp.csv", "w", newline="") as output_file:
	# 	writer = csv.writer(output_file)
	# 	writer.writerow(["Experiment: ", "Straight, 3d, sequence 8, it: 1000"])

	# 	for row in scores:
	# 		writer.writerow(row)







