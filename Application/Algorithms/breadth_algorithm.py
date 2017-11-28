from Classes import AminoAcidChain
import copy

# global variables
input_chain = []
chain_list = []
best_chain = []

def fold(input):

	# initialize input chain starting coords
	global input_chain
	input_chain = input
	input_chain[0].coordinates = [0,0]
	input_chain[1].coordinates = [0,1]
	# initialize starting chain of 2 nodes
	start_chain = [input_chain[0], input_chain[1]]
	# initialize start of the list
	global chain_list
	chain_list = [start_chain]
	# 'best_chain' is what needs to be returned.
	global best_chain
	best_chain = start_chain

	# increase the size of the chains with 1 node every loop
	for i in range (2, len(input_chain)):
		# make sure all chains are the same (maximum) size
		while len(chain_list[0]) < i + 1:
			# pop chain from list
			temp_chain = chain_list.pop(0)
			# check possible places for the new node
			possibilities = checkPossibilities(temp_chain, i)
			# build the new chain(s)
			buildChain(temp_chain, i, possibilities)
			
	return best_chain

	
	
def buildChain(temp_chain, i, possibilities):

	global input_chain
	global chain_list
	global best_chain
	
	# make a new (possible) chain
	for option in possibilities:
		new_chain = temp_chain[:]
		new_node = copy.copy(input_chain[i])
		new_node.coordinates = option
		new_chain.append(new_node)
		chain_list.append(new_chain)
		
		# check the scores of both the old and new chain
		previous_acid_chain = AminoAcidChain.Amino_acid_chain()
		new_acid_chain = AminoAcidChain.Amino_acid_chain()
		
		previous_acid_chain.chain = best_chain
		new_acid_chain.chain = new_chain
		
		if(new_acid_chain.stability() <= previous_acid_chain.stability()):
			best_chain = copy.copy(new_chain)
			
		
# check possible positions a new node can be placed at
def checkPossibilities(temp_chain, i):
	# remember coordinates of last amino acid in current chain
	x = temp_chain[i - 1].coordinates[0]
	y = temp_chain[i - 1].coordinates[1]
	# create array containing possible positions
	options = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
	
	# removes invalid options from the array
	for j in temp_chain:
		for option in options:
			if j.coordinates == option:
				options.remove(option)
	
	return options
	
#def checkDuplicates():
		