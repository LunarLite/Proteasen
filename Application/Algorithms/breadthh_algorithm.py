# breadthh_algorithm.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the Breadth-first algorithm with pruning
# 
# Able to fold amino acid chains consisting of up to 19 amino acids (H / P)
# --> first two H / P chains
# 		Runtime: aprox. 1.5 seconds
# 

from Classes import AminoAcidChain
from collections import deque
import copy
import math

# global variables
input_chain = []
chain_deque = deque()
best_chain = []
best_score = 0

# required domain calculation
dynamic_length = 0

# required score calculation
passed_hydro = 0


def execute(input):
	
	# initialize input chain starting coords
	global input_chain
	input_chain = input.chain
	input_chain[0].coordinates = [0,0]
	input_chain[1].coordinates = [0,1]

	
	# determine x&y domain based on chain length
	global dynamic_length
	if(len(input_chain) < 10):
		dynamic_length = math.floor(math.sqrt(len(input_chain)))
	else:
		dynamic_length = math.floor(math.sqrt(len(input_chain)))-1

	# initialize starting chain, consisting of first 2 nodes
	start_chain = [input_chain[0], input_chain[1]]
	
	# initialize start of the deque
	global chain_deque
	chain_deque.append(start_chain)
	

	global passed_hydro
	
	
	# increase the size of the chains with 1 node every loop
	for i in range (2, len(input_chain)):
		while len(chain_deque[0]) < i + 1:
			# pop chain from list
			temp_chain = chain_deque.popleft()    
			# check possible places for the new node
			possibilities = checkPossibilities(temp_chain, i)
			# get possible builds
			builds = formChain(temp_chain, i, possibilities)
			# build new chains
			buildChains(builds, i)				

		if (input_chain[i].molecule_type == "hydrophobic"):
			passed_hydro += 1
			
	# 'best_chain' is the chain that needs to be returned.
	global best_chain
	input.chain = best_chain
	return input

def formChain(temp_chain, i, possibilities):

	global input_chain
	builds = []
	
	# make a new (possible) chain
	for option in possibilities:
		new_chain = temp_chain[:]
		new_node = copy.copy(input_chain[i])
		new_node.coordinates = option
		new_chain.append(new_node)
		builds.append(new_chain)

	return builds
	
def buildChains(builds, i):

	global chain_deque
	global best_chain
	global best_score
	global passed_hydro
	
	for build in builds:
		
		# check the scores of both the old and new chain
		new_acid_chain = AminoAcidChain.Amino_acid_chain("p")
		new_acid_chain.chain = build
		new_acid_chain.stability()
		new_score = new_acid_chain.score
		
		if(new_score <= best_score):
			best_chain = build
			best_score = new_score
		
		# time to prune?
		if (i % 10 == 0):
			# what score should be pruned at
			if (new_score <= -1*(passed_hydro/2)):
				chain_deque.append(build)
		else:
			chain_deque.append(build)
			
		
# check possible positions a new node can be placed at
def checkPossibilities(temp_chain, i):

	global dynamic_length
	
	# remember coordinates of last amino acid in current chain
	x = temp_chain[i - 1].coordinates[0]
	y = temp_chain[i - 1].coordinates[1]
	# create array containing possible positions
	options = []

		
	# check for any new position if they fall within the allowed domain before adding
	if(x - 1 >= -dynamic_length):
		options.append([x - 1, y])
	if(x + 1 <= dynamic_length):
		options.append([x + 1, y])
	if(y - 1 >= -dynamic_length + 1):
		options.append([x, y - 1])
	if(y + 1 <= dynamic_length):
		options.append([x, y + 1])
	
	# removes invalid options from the array
	for j in temp_chain:
		if j.coordinates in options:
			options.remove(j.coordinates)
	
	return options