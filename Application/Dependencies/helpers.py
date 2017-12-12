# helpers.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains helpers functions: 
# > fold_random()
#


from Classes import AminoAcidChain
from random import randint
import copy

def fold_random(input_chain):
	""" This function takes as input an unfolded Amino_acid_chain object
	 and returns it folded randomly."""

	output_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)
	# iterate over each aminoacid

	for i in range (1, len(input_chain.chain)):

		# remember coordinates of previous amino acid
		x = output_chain.chain[i - 1].coordinates[0]
		y = output_chain.chain[i - 1].coordinates[1]

		# create array containing possible positions
		options = [[x + 1, y, 0], [x - 1, y, 0], [x, y + 1, 0], [x, y - 1, 0]]

		# keep track of (the amount of) conflicts
		conflict = True
		conflicts = 0;

		while conflict:

			# if conflicts more than 20, chain is probably stuck, break
			if conflicts >= 20:
				conflict = False
				break

			# randomly choose one of the possible positions
			option = randint(0, 3)
			coordinates = options[option]
			
			# iterate over all previously positioned amino acids
			for j in range(0, i):

				# if coordinates match, break to choose new coordinates
				if coordinates == output_chain.chain[j].coordinates:
					conflict = True	
					conflicts += 1
					break

				# if none of the previous coordinates match, break out of while loop
				else: 
					conflict = False	
		
		if conflicts < 20:

			# set coordinates of current amino acid
			output_chain.chain[i].coordinates = coordinates

		else:
			break;

	#if chain stuck in conflict, set coordinates back and fold again
	if conflicts >= 20:
		output_chain = fold_random(input_chain)

	return output_chain	

def ask_for_iterations():
	"""ask user to input number of iterations"""
	
	while True:
		iterations = input("Give number of iterations to execute hillclimber (500 RCMD): ")
	
		if iterations != "": 
			if str.isdigit(iterations): 
				break
	return int(iterations)
