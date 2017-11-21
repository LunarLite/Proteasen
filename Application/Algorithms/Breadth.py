from Classes import AminoAcidChain

count = 0

def fold(input):

	# initialization of globals
	global input_chain
	input_chain = input
	# [0] is 0,0 by default and [1] position doesn't matter
	input_chain[1].coordinates = [0,1]
	
	# make new acid chain and add first 2 acids
	global test_chain 
	test_chain = AminoAcidChain.Amino_acid_chain()
	test_chain.chain.append(input_chain[0])
	test_chain.chain.append(input_chain[1])

	# initialize archive to store possible chains
	global archive
	archive = []
	archive.append(test_chain)
	
	global count
	result = 0

	
	for i in range (2, len(input_chain)):
	
		possibilities = checkPossibilities(i)
		for chain in archive:
			buildChain(chain, i, possibilities)
			
		archive = temp_archive

	for chain in archive:
		score = chain.stability()
		if score >= result:
			result = score
			best_chain = chain
	return best_chain
	
def buildChain(start_chain, i, options):
	
	global temp_archive
	temp_archive = []
	
	for option in options:
		temp_chain = start_chain
		input_chain[i].coordinates = option
		temp_chain.chain.append(input_chain[i])
		# removeDuplicates(temp_chain)
		temp_archive.append(temp_chain)
		
def checkPossibilities(i):
	# remember coordinates of previous amino acid
	x = test_chain.chain[i - 1].coordinates[0]
	y = test_chain.chain[i - 1].coordinates[1]
	
	# create array containing possible positions
	option1 = [x + 1, y]
	option2 = [x - 1, y]
	option3 = [x, y + 1]
	option4 = [x, y - 1]

	options = [option1, option2, option3, option4]
	
	# removes invalid options from the array
	to_remove = []
	for j in test_chain.chain:
		for option in options:
			if j.coordinates == option:
				to_remove.append(option)
	for option in to_remove:
		options.remove(option)
			
	return options
	
#def removeDuplicates():
		