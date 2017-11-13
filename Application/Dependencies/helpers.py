from Classes import AminoAcid, AminoAcidChain


amino_acid_chain = AminoAcidChain.Amino_acid_chain()

# Creates a list of aminoacids by given comment line argument consisting of H and P.
# Returns error when comment line argument contains characters other than H or P. 
def load(input):

	# Iterate over each character in command line argument. 
	for c in input:

		# Allow only H and P in command line argument. 
		# Set molecule type to either hydrophobic or polair, as H or P indicates.
		if (c.upper() == 'H'):
			molecule_type = "hydrophobic"

		elif (c.upper() == 'P'):
			molecule_type = "polair"

		else: 
			sys.exit("Usage: python program.py HPPHHPPHH algorithm")

		# Create amino acid with appropriate type and append it to the chain.
		amino_acid_chain.add_amino(molecule_type)
	return amino_acid_chain
	
	


		
