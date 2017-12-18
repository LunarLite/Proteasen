# depth_algorithm.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the Depth-first algorithm,
# that uses the priority-queue principle based on an amino_acid_chain's score.
#
#
# > Able to fold amino acid chains consisting of up to 14 amino acids (H / P)
# --> first H/P chain (2D)
#		Runtime: aprox. 10 seconds
# 

# imports
from Classes import AminoAcidChain
from collections import deque
import copy
import math
import timeit

# variables used for score checking
best_chain = []
best_score = 0
new_acid_chain = AminoAcidChain.Amino_acid_chain("p")

def execute(input, d, max_time):
	"""Search for the best possible chain, utilizing the Depth-first method.
	If this takes more than 15 seconds, quit and return the best solution found.
	
	Keyword arguments:
	input -- the chain to work with (contains acid type and default coordinates, [0,0,0]).
	d -- determines the dimension to work in, 2D/3D.
	max_time -- determines how long the function is allowed to run.
    """
	
	
	# initialize timer
	start = timeit.default_timer()
	# initialize input chain with starting coords
	input_chain = input.chain
	input_chain[0].coordinates = [0,0,0]
	input_chain[1].coordinates = [0,1,0]
	# initialize starting chain, consisting of first 2 nodes
	start_chain = [input_chain[0], input_chain[1]]
	# initialize start of the deque
	chain_deque = deque()
	chain_deque.append(start_chain)
	input_lenght = len(input_chain)
	
	# increase the size of the chains with 1 node every loop
	while chain_deque:
	
		# stop running after max_time (15) seconds
		update = timeit.default_timer()
		if update - start > max_time:
			input.chain = best_chain
			print("Took too long, stopped after ", max_time, " seconds.")
			return False
		# pop last chain from list
		temp_chain = chain_deque.pop()
		length = len(temp_chain)
		
		# check whether to add another amino_acid or to check score and finish a chain.
		if length is not input_lenght:
			# check possible places for the new node
			possibilities = checkPossibilities(temp_chain, length, d)
			# get possible builds
			builds = formChain(temp_chain, length, possibilities, input_chain)
			# build new chains
			chain_deque = buildChains(new_acid_chain, builds, chain_deque)
		else:
			# check score
			checkScore(temp_chain)

	# return the best-scoring chain
	input.chain = best_chain
	return True

def formChain(temp_chain, i, possibilities, input_chain):
	"""Build new chains based on the possible locations of the new acid..
	
	Keyword arguments:
	temp_chain -- the starting chain to build from
	i -- the current length of temp_chain
	possibilities -- the possible ways to fold
	input_chain -- the chain of which you copy amino_acids
    """

	builds = []
	# make a new (possible) chain
	for option in possibilities:
		new_chain = temp_chain[:]
		new_node = copy.copy(input_chain[i])
		new_node.coordinates = option
		new_chain.append(new_node)
		builds.append(new_chain)

	# return all possible builds
	return builds
	
def buildChains(new_acid_chain, builds, chain_deque):
	"""Add new possible chains to chain_deque in order of (ascending) score.
	
	Keyword arguments:
	new_acid_chain -- the amino_acid_chain object, to use the score function with.
	builds -- possible new chains
	chain_deque -- the encapsulating list
    """
	scores = []
	
	# add scores to a list
	for build in builds:
		new_acid_chain.chain = build
		new_acid_chain.stability()
		scores.append(new_acid_chain.score)
	
	# sort chains based on scores, append in order of ascending score.
	sorted_builds = [x for (y,x) in sorted(zip(scores, builds), key=lambda pair: pair[0])]
	for build in sorted_builds:
		chain_deque.append(build)
			
	return chain_deque

def checkPossibilities(temp_chain, i, dimension):
	"""Check possible positions for the next amino_acid in line.
	
	Keyword arguments:
	temp_chain -- the current build the algorithm is working with.
	i -- current length of temp_chain
    """

	# remember coordinates of last amino acid in current chain
	x = temp_chain[i - 1].coordinates[0]
	y = temp_chain[i - 1].coordinates[1]
	z = temp_chain[i - 1].coordinates[2]

	# create array containing possible positions
	options = [[x - 1, y, z], [x + 1, y, z], [x, y - 1, z], [x, y + 1, z]]
	
	if dimension == "3d":
		options.append([x, y, z + 1])
		options.append([x, y, z - 1])

	# removes invalid options from the array
	for j in temp_chain:
		if j.coordinates in options:
			options.remove(j.coordinates)
	
	return options	
	
def checkScore(temp_chain):
	"""Check the score of a chosen folding and store it in best_chain and best_score,
	if it's better than the previous best.
	
	Keyword arguments:
	temp_chain -- the current chain you're iteratingthrough
    """
	
	global new_acid_chain
	global best_chain
	global best_score

	
	# check the scores of both the old and new chain
	new_acid_chain.chain = temp_chain
	new_acid_chain.stability()
	new_score = new_acid_chain.score
	
	# store new one in best, if it's better or equal than the best.
	if(new_score <= best_score):
		best_chain = temp_chain
		best_score = new_score