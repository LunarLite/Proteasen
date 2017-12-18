# breadthh_algorithm.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the Breadth-first algorithm (with heuristic pruning)
# 
# > Able to fold amino acid chains consisting of up to 20~ amino acids (H / P)
# --> first H/P chain (2D)
#		Runtime: aprox. 0.2 seconds
# --> second H/P chain (2D)
#		Runtime: aprox. 6.7 seconds
# 

from Classes import AminoAcidChain
from collections import deque
import copy
import math

# global variables
dimension = "2d"
dynamic_length = 0
passed_hydro = 0

# vars used for score checking
best_chain = []
best_score = 0
new_acid_chain = AminoAcidChain.Amino_acid_chain("p")

# vars used for beamsearch
input_lenght = 0

def execute(input, d):
	
	# set local dimension
	global dimension
	dimension = d
	# initialize input chain starting coords
	input_chain = input.chain
	input_chain[0].coordinates = [0,0,0]
	input_chain[1].coordinates = [0,1,0]
	
	# determine x&y&z domain based on chain length
	global dynamic_length
	dynamic_length = math.floor(math.sqrt(len(input_chain)))

	# initialize starting chain, consisting of first 2 nodes
	start_chain = [input_chain[0], input_chain[1]]
	# initialize start of the list
	chain_deque = deque()
	chain_deque.append(start_chain)
	
	# lenght of input, used for beamsearch and stopping at the end
	global input_lenght
	input_lenght = len(input_chain)
	
	# increase the size of the chains with 1 node every loop
	while chain_deque:
	
		# pop chain from list
		# .popleft() = breadth, .pop() = depth
		temp_chain = chain_deque.popleft()
		
		length = len(temp_chain)
		
		if length is not input_lenght:
			# check possible places for the new node
			possibilities = checkPossibilities(temp_chain, length)
			# get possible builds
			builds = formChain(temp_chain, length, possibilities, input_chain)
			# build new chains
			chain_deque = buildChains(builds, chain_deque)
			
			if len(chain_deque) > input_lenght:
				chain_deque = deque_resize_beam(chain_deque)
			
		else:
			checkScore(temp_chain)

	# 'best_chain' is the chain that needs to be returned.
	input.chain = best_chain
	return input

	
def deque_resize_beam(chain_deque):
	
	global new_acid_chain
	global input_lenght
	best_chains = []
	scores = []
	base_score = 1
	
	for i in chain_deque:
		new_acid_chain.chain = i
		new_acid_chain.stability()
		new_score = new_acid_chain.score
	
		best_chains.append(i)
		scores.append(copy.copy(new_score))
	
	sorted_builds = [x for (y,x) in sorted(zip(scores, best_chains), key=lambda pair: pair[0])]
	best_chains = sorted_builds[0:input_lenght]

	chain_deque.clear()
	for i in best_chains:
		
		chain_deque.append(i)
	return chain_deque
		
	
def formChain(temp_chain, i, possibilities, input_chain):


	builds = []
	# make a new (possible) chain
	for option in possibilities:
		new_chain = temp_chain[:]
		new_node = copy.copy(input_chain[i])
		new_node.coordinates = option
		new_chain.append(new_node)
		builds.append(new_chain)

	return builds
	
def buildChains(builds, chain_deque):
	
	for build in builds:
		chain_deque.append(build)
			
	return chain_deque

# check possible positions a new node can be placed at
def checkPossibilities(temp_chain, i):

	global dynamic_length
	# remember coordinates of last amino acid in current chain
	x = temp_chain[i - 1].coordinates[0]
	y = temp_chain[i - 1].coordinates[1]
	z = temp_chain[i - 1].coordinates[2]

	# create array containing possible positions
	options = []
	
	# check for any new position if they fall within the allowed domain before adding
	if(x - 1 >= -dynamic_length):
		options.append([x - 1, y, z])
	if(x + 1 <= dynamic_length):
		options.append([x + 1, y, z])
	if(y - 1 >= -dynamic_length):
		options.append([x, y - 1, z])
	if(y + 1 <= dynamic_length):
		options.append([x, y + 1, z])
	
	global dimension
	if dimension == "3d":
		if(z - 1 >= -dynamic_length):
			options.append([x, y, z - 1])
		if(z + 1 <= dynamic_length):
			options.append([x, y, z + 1])

	# removes invalid options from the array
	for j in temp_chain:
		if j.coordinates in options:
			options.remove(j.coordinates)
	
	return options	
	
def checkScore(temp_chain):

	global new_acid_chain
	global best_chain
	global best_score

	# check the scores of both the old and new chain
	new_acid_chain.chain = temp_chain
	new_acid_chain.stability()
	new_score = new_acid_chain.score
	
	if(new_score <= best_score):
		best_chain = temp_chain
		best_score = new_score