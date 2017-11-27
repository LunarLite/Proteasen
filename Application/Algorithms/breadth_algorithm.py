from Classes import AminoAcidChain

# Global variables
input_chain = []
chain_list = []
best_chain = []

def fold(input):

	# Initialize input chain starting coords
	global input_chain
	input_chain = input
	input_chain[0].coordinates = [0,0]
	input_chain[1].coordinates = [0,1]
	# Initialize starting chain of 2 nodes
	start_chain = [input_chain[0], input_chain[1]]
	# Initialize start of the list
	global chain_list
	chain_list = [start_chain]
	# 'best_chain' is what needs to be returned.
	global best_chain
	best_chain = start_chain


	for i in range (2, len(input_chain)):
		while len(chain_list[0]) < i + 1:
			temp_chain = chain_list.pop(0)
			possibilities = checkPossibilities(temp_chain, i)
			buildChain(temp_chain, i, possibilities)

	temp_check = chain_list[1]
	for node in temp_check:
		print("coords", node.coordinates)
	temp_x = AminoAcidChain.Amino_acid_chain()
	temp_x.chain = temp_check
	for node in temp_x.chain:
		print("coords", node.coordinates)
	return best_chain
	
def buildChain(temp_chain, i, possibilities):

	global input_chain
	global chain_list
	
	for option in possibilities:
		new_chain = temp_chain[0:i]
		input_chain[i].coordinates = option
		new_chain.append(input_chain[i])
		chain_list.append(new_chain)
		

# Check possible positions a new node can be placed at
def checkPossibilities(temp_chain, i):
	# Remember coordinates of last amino acid in current chain
	x = temp_chain[i - 1].coordinates[0]
	y = temp_chain[i - 1].coordinates[1]
	# Create array containing possible positions
	options = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
	
	# Removes invalid options from the array
	for j in temp_chain:
		for option in options:
			if j.coordinates == option:
				options.remove(option)
	
	return options
	
#def checkDuplicates():
		