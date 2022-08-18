import re

medicine = ""
replace = dict()
count = 0
replacements = set()

with open("example_input.txt") as f:
    for line in f:
        words = line.split()
        try:
            replace[count] = {words[0]: words[2]}
            count += 1
        except IndexError:
            medicine = line

molecules = tuple(re.sub( r"([A-Z])", r" \1", medicine).split())
temp = list(molecules)
print(molecules)

count = 0

for i in range(len(replace)):
    for j in range(len(molecules)):
        if list(replace[i].keys())[0] == molecules[j]:
            print(f'Molecule {molecules[j]} is changed to {replace[i][molecules[j]]}')
            temp[j] = replace[i][list(replace[i].keys())[0]]
            print(temp)
            if not "".join(temp) in replacements:
                print(f'New Combination: {"".join(temp)}')
                replacements.add("".join(temp))
                count += 1
            temp[j] = molecules[j]
            print("")


print(len(replacements))


