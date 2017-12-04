import csv
import sys
from tkinter import *
from Classes import SequenceSelector


def run():
	root = Tk()
	selector = SequenceSelector.Selector_App(root)
	selector.load_sequence_list(load_sequences_from_csv())

	root.mainloop()

	sequence = selector.chosen_sequence
	if sequence == "": 
		sys.exit("You have to enter a sequence and algorithm in order to run this program")

	algorithm = selector.chosen_algorithm

	return sequence, algorithm

# skip first line https://stackoverflow.com/questions/14674275/skip-first-linefield-in-loop-using-csv-file
def load_sequences_from_csv(): 
	with open("sequences.csv", 'r') as file:
		reader = csv.reader(file)
		sequences = []
		firstline = True
		for rows in reader: 
			if firstline: 
				firstline = False 
				continue
			sequences.append(rows[1].strip())

	return sequences
		
