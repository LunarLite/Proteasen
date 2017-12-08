# breadth_algorithm.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the Breadth-first algorithm
# 
# > Able to fold amino acid chains consisting of up to 14 amino acids (H / P)
# --> first H/P chain
#		Runtime: aprox. 10 seconds
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


def execute(input):
	
	# initialize input chain starting coords
	global input_chain
	input_chain = input.chain
	input_chain[0].coordinates = [0,0]
	input_chain[1].coordinates = [0,1]

	# initialize starting chain, consisting of first 2 nodes
	start_chain = [input_chain[0], input_chain[1]]
	# initialize start of the list
	global chain_deque
	chain_deque.append(start_chain)
	
	
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
			buildChains(builds)
			
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
	
def buildChains(builds):

	global chain_deque
	global best_chain
	global best_score
	
	for build in builds:
		chain_deque.append(build)
		
		# check the scores of both the old and new chain
		new_acid_chain = AminoAcidChain.Amino_acid_chain("p")
		new_acid_chain.chain = build
		new_acid_chain.stability()
		new_score = new_acid_chain.score
		
		if(new_score <= best_score):
			best_chain = copy.copy(build)
			best_score = new_score

# check possible positions a new node can be placed at
def checkPossibilities(temp_chain, i):

	global dynamic_length
	
	# remember coordinates of last amino acid in current chain
	x = temp_chain[i - 1].coordinates[0]
	y = temp_chain[i - 1].coordinates[1]
	# create array containing possible positions
	options = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
	
	# removes invalid options from the array
	for j in temp_chain:
		if j.coordinates in options:
			options.remove(j.coordinates)
	
	return options	