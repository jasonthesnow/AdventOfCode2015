from crypt import crypt
from itertools import permutations
import re
from sys import maxsize

temp = list()

starting_compound = 'e'
medicine = ''
replacement_molecules = dict()
max_substitution = 0
min_steps = maxsize

count = 0

puzzle_input = "input.txt"

with open(puzzle_input) as f:
    for line in f:
        words = line.split()
        try:
            replacement_molecules[count] = {words[0]: words[2]}
            count += 1
        except IndexError:
            medicine = line

molecules = re.sub( r"([A-Z])", r" \1", medicine).split()

#print(medicine)

for i in range(len(replacement_molecules)):
    current_replacement = re.sub(r"([A-Z])", r" \1", replacement_molecules[i][list(replacement_molecules[i].keys())[0]]).split()
    max_substitution = max(max_substitution, len(current_replacement))

# Plan from here:

#1. Take the molecules in the current compount (molecules joined into a string) and compare them to the compounds in replacement_molecules
#2. if there is a match, switch out the current compound's molecules into the replacement molecules
#3. repeat until it is simplified down to "e"

#4. repeat until finding the minimum amount of steps necessary to simplify current compound down to e

#while not "".join(molecules) == starting_compound:



