import csv
import sys
from tkinter import *
from Classes import SequenceSelector


def select_sequence(sequences):
	root = Tk()
	sequence_selector = SequenceSelector.Sequence_Selector(root)
	sequence_selector.list_load(sequences)

	root.mainloop()

	sequence = sequence_selector.chosen_sequence
	if sequence == "": 
		sys.exit("You have to enter a sequence and algorithm in order to run this program")

	algorithm = sequence_selector.chosen_algorithm

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
			sequences.append({"id": rows[0], "sequence": rows[1].strip()})

	return sequences
		





	



	


		
