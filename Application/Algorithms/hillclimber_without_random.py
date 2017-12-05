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
	best_acid_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)


	print(input_chain.chain[3].coordinates)
	print(new_acid_chain.chain[3].coordinates)


	# fold amino acid chain straight
	for i, acid in enumerate(new_acid_chain.chain):
		acid.coordinates = [i, 0]
		print(new_acid_chain.chain[i].coordinates)


	attempts = 0
	start_score = new_acid_chain.stability()
	print("stability now: ", start_score)


	while attempts < 1000:
		rotated_coordinates = new_acid_chain.rotate(0)
		if rotated_coordinates == 1:
			print("DIT GING MIS DOEI")
			break

		print("ROTATED", rotated_coordinates)

		rotated_acid_chain.chain = rotated_coordinates
		print("ROTATED CHAIN", rotated_acid_chain)
		print("UNROTATED CHAIN", new_acid_chain)
	
		print("NIEUWE STABILITY", new_acid_chain.stability())

		if rotated_acid_chain.stability() <= new_acid_chain.stability():
			new_acid_chain.coordinates = rotated_coordinates
			# print(best_random.coordinates)
			attempts += 1
		else: 
			attempts += 1
	
	print(start_score)

	# set input chain random folded chain with best score
	input.chain = new_acid_chain.chain








