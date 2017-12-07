from Algorithms import random_algorithm
from Classes import AminoAcidChain
import copy
from Dependencies import helpers
from random import randint


def execute(input_chain, start_point):
	""" This function takes as input an unfolded Amino_acid_chain object 
	and then folds it using hillcimber, with random_folded or straight_folded 
	as a starting point."""

	# initialize variables to store temporary acid chains
	new_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	rotated_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	best_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)\


	if start_point == "straight_folded":

		# fold amino acid chain straight
		for i, acid in enumerate(new_acid_chain.chain):
			acid.coordinates = [i, 0]
			# print(new_acid_chain.chain[i].coordinates)
	
	elif start_point == "random_folded":
		new_acid_chain = helpers.fold_random(input_chain)

	attempts = 0
	new_acid_chain.stability()
	start_score = new_acid_chain.score
	# print("stability now: ", start_score)


	while attempts < 500:
		rotated_chain = new_acid_chain.rotate(0)
		if rotated_chain == 1:
			print("no possible rotations found at attempt nr", attempts)
			
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

			# increase number of attempts with 1
			attempts += 1
		else: 

			# else, increase number of attempts with 5
			attempts += 10
	
	# print start_score to show whether hillclimber improved stability
	print("Start score:", start_score)

	# set input chain random folded chain with best score
	input_chain.chain = new_acid_chain.chain








