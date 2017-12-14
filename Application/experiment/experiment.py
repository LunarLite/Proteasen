#
# experiment.py
#

# plots aminoacid chain configuration
def plot(self):
	
	# Add new subplot
	subPlot = fig.add_subplot(111)

	# create empty lists to store x and y coordinates
	x = []
	y = []

	
	# iterate over each aminoacid 
	for i in range(0, len(self.chain)):

		# store x and y coordinates of current aminoacid
		x.append(self.chain[i].coordinates[0])
		y.append(self.chain[i].coordinates[1])
	
	# subplot backbone aminoacid chain
	subPlot.plot(x, y, 'k-')
	# set subplot ticks to the exact amount required
	subPlot.set_xticks(x, False)
	subPlot.set_yticks(y, False)

	# iterate over each aminoacid
	for i in range(0, len(self.chain)):
		
		# check for type of current aminoacid
		if self.chain[i].molecule_type == "hydrophobic": 

			# plot red dot at coordinates of hydrophobic aminoacid
			subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'ro')
			plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'ro')

		elif self.chain[i].molecule_type == "polair":  

			# plot blue dot at coordinates of polair aminoacid
			subPlot.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'bo')
			plt.plot(self.chain[i].coordinates[0], self.chain[i].coordinates[1], 'bo')
	
	# draw a grid behind Subplot 
	subPlot.grid()

	# display pop-up window with plot
	plt.show()
