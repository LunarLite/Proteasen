from random import randint


def fold(amino_acid_chain):

	
	# occupied = [[0, 0]]

	# Iterate over each aminoacid.
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

		conflict = True

		while conflict:

			# randomly choose one of the possible positions
			option = randint(0, 3)
			coordinates = options[option]
			
			# iterate over all previously positioned amino acids
			for j in range(0, i):

				# if coordinates match, break to choose new coordinates
				if coordinates == amino_acid_chain[j].coordinates:
					conflict = True	
					break

				# if none of the previous coordinates match, break out of while loop
				else: 
					conflict = False	
		
		# set coordinates of current amino acid
		amino_acid_chain[i].coordinates = coordinates
