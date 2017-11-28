from random import randint
import copy

def fold_random(input_chain):
	""" This function takes as input an unfolded aminoacid chain, which is 
	the chain element of the Amino_acid_chain class, and returns it folded randomly. """

	output_chain = copy.copy(input_chain)
	# Iterate over each aminoacid.

	for i in range (1, len(input_chain)):

		# remember coordinates of previous amino acid
		x = output_chain[i - 1].coordinates[0]
		y = output_chain[i - 1].coordinates[1]

		# create array containing possible positions
		option1 = [x + 1, y]
		option2 = [x - 1, y]
		option3 = [x, y + 1]
		option4 = [x, y - 1]

		options = [option1, option2, option3, option4]

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
				if coordinates == output_chain[j].coordinates:
					conflict = True	
					conflicts += 1
					break

				# if none of the previous coordinates match, break out of while loop
				else: 
					conflict = False	
		
		if conflicts < 20:

			# set coordinates of current amino acid
			output_chain[i].coordinates = coordinates
		
		else:
			break

	#if chain stuck in conflict, set coordinates back and fold again
	if conflicts >= 20:
		output_chain = fold_random(input_chain)
	
	return output_chain	


		
