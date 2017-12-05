from Classes import AminoAcidChain
from collections import deque
import copy
import timeit
import math

# global variables
input_chain = []
chain_deque = deque()
best_chain = []

# required domain calculation
dynamic_length = 0

# required score calculation
total_hydro = 0
passed_hydro = 0

# TEMPORARY
trashcan = 0


def execute(input):
	
	# initialize input chain starting coords
	global input_chain
	input_chain = input.chain
	input_chain[0].coordinates = [0,0]
	input_chain[1].coordinates = [0,1]
	global total_hydro
	for i in input_chain:
		if (i.molecule_type == "hydrophobic"):
			total_hydro += 1
	
	# determine x&y domain based on chain length
	global dynamic_length
	#dynamic_length = (len(input_chain)/2)-(len(input_chain)/4)
	dynamic_length = math.ceil(math.sqrt(10))-math.floor((10/7))
	#dynamic_length = math.floor(math.sqrt(len(input_chain)))-2
	#dynamic_length = math.ceil(math.sqrt(len(input_chain)))-2
	# initialize starting chain of 2 nodes
	start_chain = [input_chain[0], input_chain[1]]
	# initialize start of the list
	global chain_deque
	chain_deque.append(start_chain)
	# 'best_chain' is what needs to be returned.
	global best_chain
	best_chain = start_chain
	
	# TODO
	# deque -> priority queue
	# Check score and throw away too low scores
	
	# increase the size of the chains with 1 node every loop
	for i in range (2, len(input_chain)):
		print(i+1)
		# make sure all chains are the same (maximum) size
		while len(chain_deque[0]) < i + 1:
			# pop chain from list
			temp_chain = chain_deque.popleft()    
			# check possible places for the new node
			possibilities = checkPossibilities(temp_chain, i)
			# build the new chain(s)
			buildChain(temp_chain, i, possibilities)

	input.chain = best_chain
	print("Chains thrown away: ", trashcan)
	return input

	
	
def buildChain(temp_chain, i, possibilities):

	global input_chain
	global chain_deque
	global best_chain
	global trashcan
	global dynamic_length
	global passed_hydro
	
	# make a new (possible) chain
	for option in possibilities:
		new_chain = temp_chain[:]
		new_node = copy.copy(input_chain[i])
		new_node.coordinates = option
		new_chain.append(new_node)
		

		if (new_node.molecule_type == "hydrophobic"):
			passed_hydro += 1
	
		# check the scores of both the old and new chain
		previous_acid_chain = AminoAcidChain.Amino_acid_chain()
		new_acid_chain = AminoAcidChain.Amino_acid_chain()
		
		previous_acid_chain.chain = best_chain
		new_acid_chain.chain = new_chain
		
		new_score = new_acid_chain.stability()
		previous_score = previous_acid_chain.stability()
		
		if(new_score <= previous_score):
			best_chain = copy.copy(new_chain)
		
		# time to prune?
		if (i % 10 == 0):
			dynamic_length = math.ceil(math.sqrt(i))-math.floor(i/5)+((i/10)-1)
			# what score should be pruned at
			if (new_score <= -1 -(i/10)):
				chain_deque.append(new_chain)
			else:
				trashcan += 1
		else:
			chain_deque.append(new_chain)


			
		
# check possible positions a new node can be placed at
def checkPossibilities(temp_chain, i):

	global dynamic_length
	
	# remember coordinates of last amino acid in current chain
	x = temp_chain[i - 1].coordinates[0]
	y = temp_chain[i - 1].coordinates[1]
	# create array containing possible positions
	# options = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
	options = []
	if(x - 1 >= -dynamic_length):
		options.append([x - 1, y])
	if(x + 1 <= dynamic_length):
		options.append([x + 1, y])
	if(y - 1 >= -dynamic_length):
		options.append([x, y - 1])
	if(y + 1 <= dynamic_length):
		options.append([x, y + 1])
	

	# removes invalid options from the array
	for j in temp_chain:
		if j.coordinates in options:
			options.remove(j.coordinates)
	
	return options
	
	
# checks whether a chain already exists
# def checkDuplicates(new_chain):
	
	
	
	
	
	
	
	