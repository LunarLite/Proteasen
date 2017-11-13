import AminoAcid
import sys

from random import randint
from matplotlib import pyplot as plt

# Amino acid chain. 
class Amino_acid_chain:
	def __init__(self):
		self.chain = []

	def add_amino(self, molecule_type):
		self.chain.append(AminoAcid.Amino_acid(molecule_type))

	# Determines optimal aminoacid chain configuration.
	def fold(self): 

		algorithm = str(sys.argv[2])

		if algorithm == "Random" or algorithm == "random":
			occupied = [[0, 0]]
			# Iterate over each aminoacid.
			for i in range (1, len(self.chain)):

				# create array containing possible positions
				prev_acid = self.chain[i - 1]
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

				self.chain[i].x = x
				self.chain[i].y = y
		else: 
			sys.exit("Usage: python program.py HPPHHPPHH algorithm")

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
		


