from Algorithms import random_algorithm
from Classes import AminoAcidChain
import copy

# Global variables
input_chain = []
random_list = []
best_random = []

def fold(input):

	# global input_chain
	# input_chain = input
	# global best_random
	# random_list.append(copy.copy(random_algorithm.fold(input_chain)))
	# best_random = random_list[0]

	# for i in range(1, 10):
	# 	random_list[i] = copy.copy(random_algorithm.fold(input_chain))

	# 	if random_list[i].stability() >= best_random.stability():


	# if chain stuck in conflict, set coordinates back and fold again
	# if output == 1:
	# 	for i in self.chain:
	# 		i.coordinates = [0, 0]
	# 	self.fold(algorithm)

	return input
