from matplotlib import pyplot as plt
from random import randint
from Classes import AminoAcid


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
		aminoacid_chain.append(AminoAcid.Amino_acid(molecule_type))
	return aminoacid_chain
	
	
# Determines optimal aminoacid chain configuration.
def fold(chain): 

	occupied = [[0, 0]]
	# Iterate over each aminoacid.
	for i in range (1, len(chain)):

		# create array containing possible positions
		prev_acid = chain[i - 1]
		tup1 = [prev_acid.x + 1, prev_acid.y]
		tup2 = [prev_acid.x - 1, prev_acid.y]
		tup3 = [prev_acid.x, prev_acid.y + 1]
		tup4 = [prev_acid.x, prev_acid.y - 1]

		options = [tup1, tup2, tup3, tup4]

		fout = True

		while fout:
			option = randint(0, 3)

			x = options[option][0]
			y = options[option][1]
			if [x, y] not in occupied:
				fout = False			 		

		occupied.append([x, y])
		#print(occupied)

		chain[i].x = x
		chain[i].y = y

		
# Plots aminoacid chain configuration.
def plot(chain):
	
	# Create empty lists to store x and y coordinates.
	x = []
	y = []

	# Iterate over each aminoacid. 
	for i in range(0, len(chain)):

		# Store x and y coordinates of current aminoacid.
		x.append(chain[i].x)
		y.append(chain[i].y)
	
	# Plot backbone aminoacid chain.
	plt.plot(x, y, 'k-')

	# Iterate over each aminoacid.
	for i in range(0, len(chain)):
		
		# Check for type of current aminoacid. 
		if chain[i].molecule_type == "hydrophobic": 

			# Plot red dot at coordinates of hydrophobic aminoacid.
			plt.plot(chain[i].x, chain[i].y, 'ro')

		elif chain[i].molecule_type == "polair":  

			# Plot blue dot at coordinates of polair aminoacid.
			plt.plot(chain[i].x, chain[i].y, 'bo')
	
	# Draw a grid behind plots. 
	plt.grid()

	# Display pop-up window with plot. 
	plt.show()
	
