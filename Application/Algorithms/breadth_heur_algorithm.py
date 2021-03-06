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
dynamic_length = 0
# variables used for score checking
best_chain = []
best_score = 0
new_acid_chain = AminoAcidChain.Amino_acid_chain("p")
# variables used for beamsearch
input_lenght = 0

def execute(input, d):
	"""Search for the best possible chain, utilizing the Breadth-first method.
	Adds in 2 seperate heurstics:
	Restricts used domain on the x/y/z axis.
	Utilizes beam-search, only keeping the best input_length options based on score.
	
	Keyword arguments:
	input -- the chain to work with (contains acid type and default coordinates, [0,0,0]).
	d -- determines the dimension to work in, 2D/3D.
    """
	
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
	
		# pop chain from deque
		temp_chain = chain_deque.popleft()
		length = len(temp_chain)
		
		# determine whether to continue building, or to finish a chain and determine it's score
		if length is not input_lenght:
			# check possible places for the new node
			possibilities = checkPossibilities(temp_chain, length, d)
			# get possible builds
			builds = formChain(temp_chain, length, possibilities, input_chain)
			# build new chains
			chain_deque = buildChains(builds, chain_deque)
			# check wether to apply resizing based on the beam_search
			if len(chain_deque) > input_lenght:
				chain_deque = deque_resize_beam(chain_deque)
		else:
			checkScore(temp_chain)

	# return the best scoring chain
	input.chain = best_chain
	return input

def deque_resize_beam(chain_deque):
	"""Checks the score of all chains in chain_deque, keeps (up to input_length) of the best.
	
	Keyword arguments:
	chain_deque -- the deque object which to iterate through.
    """
	global new_acid_chain
	global input_lenght
	best_chains = []
	scores = []
	base_score = 1
	
	# store all chains and their corresponding score
	for i in chain_deque:
		new_acid_chain.chain = i
		new_acid_chain.stability()
		new_score = new_acid_chain.score
	
		best_chains.append(i)
		scores.append(copy.copy(new_score))
	# sort the stored chains based on their score, keep only the 0-input_length first
	sorted_builds = [x for (y,x) in sorted(zip(scores, best_chains), key=lambda pair: pair[0])]
	best_chains = sorted_builds[0:input_lenght]

	# replace deque content with the remaining chains and return deque
	chain_deque.clear()
	for i in best_chains:
		chain_deque.append(i)
		
	return chain_deque
		
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

	return builds
	
def buildChains(builds, chain_deque):
	"""Add new possible chains to chain_deque in order of (ascendind) score.
	
	Keyword arguments:
	new_acid_chain -- the amino_acid_chain object, to use the score function with.
	builds -- possible new chains
	chain_deque -- the encapsulating list
    """
	
	# add new chains to the deque
	for build in builds:
		chain_deque.append(build)
			
	return chain_deque

def checkPossibilities(temp_chain, i, dimension):
	"""Check possible positions for the next amino_acid in line, 
	But don't allow them to placed outside of a certain domain.
	This domain is based on global "dynamic_length".
	
	Keyword arguments:
	temp_chain -- the current build the algorithm is working with.
	i -- current length of temp_chain
    """
	
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
	# replace best_chain and best_score if new_score scores better
	if(new_score <= best_score):
		best_chain = temp_chain
		best_score = new_score