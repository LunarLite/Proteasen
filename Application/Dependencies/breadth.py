from Classes import AminoAcidChain

def fold(input_chain):

	# initialize archive to store possible chains
	archive = []

	for acid in input_chain[0]:


	archive.push(amino_acid_chain[0])
	chain =

	amino_acid_chain[1].coordinates[0] = 1
	amino_acid_chain[1].coordinates[1] = 0
	for i in range (1, len(amino_acid_chain)):

		# remember coordinates of previous amino acid
		x = amino_acid_chain[i - 1].coordinates[0]
		y = amino_acid_chain[i - 1].coordinates[1]

		# create array containing possible positions
		option1 = [x + 1, y]
		option2 = [x - 1, y]
		option3 = [x, y + 1]
		option4 = [x, y - 1]

		options = [option1, option2, option3, option4]

		for j in range(options):

