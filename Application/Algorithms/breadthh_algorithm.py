from Classes import AminoAcidChain
from collections import deque
import copy
import timeit
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

# statistics
trashcan = 0


def execute(input):
	
	# initialize input chain starting coords
	global input_chain
	input_chain = input.chain
	input_chain[0].coordinates = [0,0]
	input_chain[1].coordinates = [0,1]

	
	# determine x&y domain based on chain length
	global dynamic_length
	#dynamic_length = math.ceil(math.sqrt(10))-math.floor(10/7)
	dynamic_length = math.ceil(len(input_chain)/4)-1

	# initialize starting chain of 2 nodes
	start_chain = [input_chain[0], input_chain[1]]
	# initialize start of the list
	global chain_deque
	chain_deque.append(start_chain)
	


	global passed_hydro
	
	# increase the size of the chains with 1 node every loop
	for i in range (2, len(input_chain)):
		print(i+1)

		while len(chain_deque[0]) < i + 1:
			# pop chain from list
			temp_chain = chain_deque.popleft()    
			# check possible places for the new node
			possibilities = checkPossibilities(temp_chain, i)
			# build the new chain(s)
			buildChain(temp_chain, i, possibilities)
			
				

		if (input_chain[i].molecule_type == "hydrophobic"):
			passed_hydro += 1

	# temporary statistics
	print("Chains thrown away: ", trashcan)
			
	# 'best_chain' is the chain that needs to be returned.
	global best_chain
	input.chain = best_chain
	return input

	
	
def buildChain(temp_chain, i, possibilities):

	global input_chain
	global chain_deque
	global best_chain
	global best_score
	global trashcan
	global dynamic_length
	global passed_hydro
	
	# make a new (possible) chain
	for option in possibilities:
		new_chain = temp_chain[:]
		new_node = copy.copy(input_chain[i])
		new_node.coordinates = option
		new_chain.append(new_node)
	
		# check the scores of both the old and new chain
		new_acid_chain = AminoAcidChain.Amino_acid_chain("p")
		new_acid_chain.chain = new_chain
		new_acid_chain.stability()
		new_score = new_acid_chain.score
		

		if(new_score <= best_score):
			best_chain = copy.copy(new_chain)
			best_score = new_score
		
		
		# time to prune?
		if (i % 10 == 0):
			# dynamic_length = math.ceil(math.sqrt(i))-math.ceil(i/5)+(i/10)
			
			# what score should be pruned at
			if (new_score <= -1*(passed_hydro/2)):
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
	options = []

		
	# check for any new position if they fall within the allowed domain before adding
	if (math.sqrt(math.pow(x + 1, 2) + math.pow(y,2)) <= dynamic_length):
		options.append([x - 1, y])
	if (math.sqrt(math.pow(x - 1, 2) + math.pow(y,2)) <= dynamic_length):
		options.append([x + 1, y])
	if (math.sqrt(math.pow(x, 2) + math.pow(y - 1,2)) <= dynamic_length):
		options.append([x, y - 1])
	if (math.sqrt(math.pow(x, 2) + math.pow(y + 1,2)) <= dynamic_length):
		options.append([x, y + 1])
	
	# removes invalid options from the array
	for j in temp_chain:
		if j.coordinates in options:
			options.remove(j.coordinates)
	
	return options