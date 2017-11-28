from random import randint


def fold(amino_acid_chain):

	# iterate over each aminoacid
	for i in range (1, len(amino_acid_chain)):

		# remember coordinates of previous amino acid
		x = amino_acid_chain[i - 1].coordinates[0]
		y = amino_acid_chain[i - 1].coordinates[1]

		# create array containing possible positions
		options = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]

		# keep track of (the amount of) conflicts
		conflict = True
		conflicts = 0;

		while conflict:

			# if conflicts more than 20, chain is probably stuck, break
			if conflicts > 20:
				print("large conflict")
				conflict = False
				break

			# randomly choose one of the possible positions
			option = randint(0, 3)
			coordinates = options[option]
			
			# iterate over all previously positioned amino acids
			for j in range(0, i):

				# if coordinates match, break to choose new coordinates
				if coordinates == amino_acid_chain[j].coordinates:
					conflict = True	
					conflicts += 1
					break

				# if none of the previous coordinates match, break out of while loop
				else: 
					conflict = False	
		
		if conflicts < 20:

			# set coordinates of current amino acid
			amino_acid_chain[i].coordinates = coordinates
		
		else:
			break

	# return error to fold again is conflicts > 20
	if conflicts >= 20:
		return 1
	else:
		return 0
