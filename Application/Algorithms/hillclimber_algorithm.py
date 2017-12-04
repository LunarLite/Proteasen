from Algorithms import random_algorithm
from Classes import AminoAcidChain
import copy
from Dependencies import helpers
from random import randint

# Global variables
# input_chain = []
random_list = []
best_random = []

def execute(input):

	# initialize variables to store temporary acid chains
	best_random = AminoAcidChain.Amino_acid_chain()
	new_acid_chain = AminoAcidChain.Amino_acid_chain()
	rotated_acid_chain = AminoAcidChain.Amino_acid_chain()

	# random_list.append(random(input))
	# best_random.chain = random_list[0]
	# best_score = 0


	for i in range(10):

		# print("huidige beste score: ", best_random.stability())
		random_list.append(helpers.fold_random(input.chain))
		new_acid_chain.chain = random_list[i]

		if i == 0:
			best_score = copy.copy(new_acid_chain.stability())
			best_random = copy.deepcopy(new_acid_chain)

		elif new_acid_chain.stability() <= best_random.stability():
			# print("hogere of gelijke score: ", new_acid_chain.stability(), best_random.stability())
			best_random = copy.deepcopy(new_acid_chain)
			best_score = best_random.stability()
		else:
			print("niet hoger", new_acid_chain.stability())

	attempts = 0
	start_score = copy.deepcopy(best_random.stability())
	# print("stability now: ", best_random.stability())
	while attempts < 1000:
		rotated_coordinates = best_random.rotate(0)
		if rotated_coordinates == 1:
			# print("DIT GING MIS DOEI")
			break
		# print("ROTATED: ", rotated_coordinates)
		new_acid_chain.coordinates = rotated_coordinates
		
		# print("NIEUWE STABILITY", new_acid_chain.stability())

		if new_acid_chain.stability() <= best_random.stability():
			best_random.coordinates = rotated_coordinates
			# print(best_random.coordinates)
			attempts += 1
		else: 
			attempts += 1
	
	# print(start_score, best_random.coordinates)

	# set input chain random folded chain with best score
	input.coordinates = best_random.coordinates








