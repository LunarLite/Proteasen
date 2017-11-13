import AminoAcid
from random import randint
from matplotlib import pyplot as plt

# Amino acid chain. 
class Amino_acid_chain:
	def __init__(self):
		self.chain = []
		self.length = 0

	def add_amino(self, molecule_type):
		self.chain.append(AminoAcid.Amino_acid(molecule_type))
		self.length += 1

	# Determines optimal aminoacid chain configuration.
	def fold(self): 

		occupied = [[0, 0]]
		# Iterate over each aminoacid.
		for i in range (1, len(self.chain)):

			# create array containing possible positions
			prev_acid = self.chain[i - 1]
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

			self.chain[i].x = x
			self.chain[i].y = y

	# Plots aminoacid chain configuration.
	def plot(self):
		
		# Create empty lists to store x and y coordinates.
		x = []
		y = []

		# Iterate over each aminoacid. 
		for i in range(0, len(self.chain)):

			# Store x and y coordinates of current aminoacid.
			x.append(self.chain[i].x)
			y.append(self.chain[i].y)
		
		# Plot backbone aminoacid chain.
		plt.plot(x, y, 'k-')

		# Iterate over each aminoacid.
		for i in range(0, len(self.chain)):
			
			# Check for type of current aminoacid. 
			if self.chain[i].molecule_type == "hydrophobic": 

				# Plot red dot at coordinates of hydrophobic aminoacid.
				plt.plot(self.chain[i].x, self.chain[i].y, 'ro')

			elif self.chain[i].molecule_type == "polair":  

				# Plot blue dot at coordinates of polair aminoacid.
				plt.plot(self.chain[i].x, self.chain[i].y, 'bo')
		
		# Draw a grid behind plots. 
		plt.grid()

		# Display pop-up window with plot. 
		plt.show()
		


