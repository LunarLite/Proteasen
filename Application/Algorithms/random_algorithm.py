# random_algorithm.py
#
# Heuristics - Protein Pow(d)er
# http://heuristieken.nl/wiki/index.php?title=Protein_Pow(d)er
#
# Students: Mick Tozer, Eline Rietdijk and Vanessa Botha
#
# this file contains the Random algorithm
# gives the best chain of 40 randomly folded amino acid chains
#
# Able to fold amino acid chains consisting of > 49 amino acids (H / P)
# --> all of the H/P chains
# 		Runtime: > 0,05 seconds
#
# 

from Classes import AminoAcidChain
from Dependencies import helpers
from random import randint


def execute(input_chain):
	"""This function takes as input an unfolded Amino_acid_chain object, 
	folds it randomly 40 times, and returns the chain with the best score."""

	# create new chain with sequence of input chain
	new_random_chain = AminoAcidChain.Amino_acid_chain(input_chain.sequence)

	for i in range (40):

		# fold random new chain and calculate stability score
		new_random_chain = helpers.fold_random(new_random_chain)
		new_random_chain.stability()

		# if score of new chain is higher than current input_chain
		if new_random_chain.score < input_chain.score:

			# fold input_chain like new chain and update score
			input_chain.chain = new_random_chain.chain
			input_chain.stability()

	# if score of best radom is still 0, fold like new_random_chain
	if input_chain.score == 0:
		input_chain.chain = new_random_chain.chain

