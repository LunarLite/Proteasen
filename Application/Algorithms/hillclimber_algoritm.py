from Algorithms import random_algorithm
from Classes import AminoAcidChain
import copy

# Global variables
input_chain = []
random_list = []
best_random = []

def fold(input):

	global input_chain
	input_chain = input

	for i in range(10)
		output[i] = random_algorithm.fold(copy.copy(input_chain))

	# if chain stuck in conflict, set coordinates back and fold again
	if output == 1:
		for i in self.chain:
			i.coordinates = [0, 0]
		self.fold(algorithm)
