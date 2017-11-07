from matplotlib import pyplot as plt
from Classes.AminoAcid import *

aminoacid_chain = []

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
			sys.exit("Usage: python program.py HPPHHPPHH")

		# Create aminoacid with appropriate type and append it to the chain.
		aminoacid_chain.append(Amino_acid(molecule_type))
	return aminoacid_chain
	
	
# Plots aminoacid chain configuration.
def plot():
	
	# Create empty lists to store x and y coordinates.
	x = []
	y = []

	# Iterate over each aminoacid. 
	for i in range(0, len(aminoacid_chain)):

		# Store x and y coordinates of current aminoacid.
		x.append(aminoacid_chain[i].x)
		y.append(aminoacid_chain[i].y)
	
	# Plot backbone aminoacid chain.
	plt.plot(x, y, 'k-')

	# Iterate over each aminoacid.
	for i in range(0, len(aminoacid_chain)):
		
		# Check for type of current aminoacid. 
		if aminoacid_chain[i].molecule_type == "hydrophobic": 

			# Plot red dot at coordinates of hydrophobic aminoacid.
			plt.plot(aminoacid_chain[i].x, aminoacid_chain[i].y, 'ro')

		elif aminoacid_chain[i].molecule_type == "polair":  

			# Plot blue dot at coordinates of polair aminoacid.
			plt.plot(aminoacid_chain[i].x, aminoacid_chain[i].y, 'bo')
	
	# Draw a grid behind plots. 
	plt.grid()

	# Display pop-up window with plot. 
	plt.show()