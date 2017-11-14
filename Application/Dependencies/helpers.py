from random import randint


def random(amino_acid_chain):
	occupied = [[0, 0]]

	# Iterate over each aminoacid.
	for i in range (1, len(amino_acid_chain)):

		# create array containing possible positions
		prev_acid = amino_acid_chain[i - 1]
		option1 = [prev_acid.x + 1, prev_acid.y]
		option2 = [prev_acid.x - 1, prev_acid.y]
		option3 = [prev_acid.x, prev_acid.y + 1]
		option4 = [prev_acid.x, prev_acid.y - 1]

		options = [option1, option2, option3, option4]

		error = True

		while error:
			option = randint(0, 3)

			x = options[option][0]
			y = options[option][1]
			if [x, y] not in occupied:
				error = False			 		

		occupied.append([x, y])
		#print(occupied)

		amino_acid_chain[i].x = x
		amino_acid_chain[i].y = y
	return amino_acid_chain

	


		
