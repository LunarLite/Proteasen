from Algorithms import random_algorithm
from Classes import AminoAcidChain
import copy
from Dependencies import helpers
from random import randint

# Global variables
# input_chain = []
random_list = []
best_random = []

def execute(input_chain):

	# initialize variables to store temporary acid chains
	# best_random = AminoAcidChain.Amino_acid_chain()
	new_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	rotated_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	best_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)\


	# fold amino acid chain straight
	for i, acid in enumerate(new_acid_chain.chain):
		acid.coordinates = [i, 0]
		# print(new_acid_chain.chain[i].coordinates)


	attempts = 0
	new_acid_chain.stability()
	start_score = new_acid_chain.score
	# print("stability now: ", start_score)


	while attempts < 500:
		rotated_chain = new_acid_chain.rotate(0)
		if rotated_chain == 1:
			print("DIT GING MIS DOEI")
			break


		rotated_acid_chain.chain = rotated_chain
		# for acid in rotated_acid_chain.chain:
		# 	print(acid.coordinates)

		rotated_acid_chain.stability()

		# print("NIEUWE STABILITY", rotated_acid_chain.score)

		if rotated_acid_chain.score <= new_acid_chain.score:
			new_acid_chain.chain = rotated_chain
			new_acid_chain.stability()
			attempts += 1
		else: 
			attempts += 1
	
	print(start_score)

	# set input chain random folded chain with best score
	input_chain.chain = new_acid_chain.chain








