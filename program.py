# imports
import sys


# object that can be either a hydrophobic or polar
class Aminozuur:
	def __init__(self, type, x, y):
		self.type = type
		position_x = x
		position_y = y

# main execution
if __name__ == '__main__':
	# stuff to run
	if (len(sys.argv) != 2):
		sys.exit("Usage: python program.py HPPHHPPHH")

	print("Given srting: " + str(sys.argv[1]))
	