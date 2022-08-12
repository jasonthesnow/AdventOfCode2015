from itertools import permutations

#List of variables we need:
    # 1. Each person
    # 2. The Like/Dislike of sitting next to them
    # 3. Total average happiness

puzzle_input = "input.txt"

people = set()
ind_happiness = dict()

current_happiness = 0;

max_happiness = 0;




# Reading all the lines of the file, taking the information and applying it to variables
with open(puzzle_input) as f:
    for line in f:
        line_split = line.split()
        line_split[10] = line_split[10].strip('.')
        ind_happiness[f'{line_split[0]}.Me'] = 0
        ind_happiness[f'Me.{line_split[0]}'] = 0
        if line_split[2] == "gain":
            ind_happiness[f'{line_split[0]}.{line_split[10]}'] = int(line_split[3])
        elif line_split[2] == "lose":
            ind_happiness[f'{line_split[0]}.{line_split[10]}'] = -int(line_split[3])
        else:
            print("It Broken")
        people.add(line_split[0])


        print(f"{line_split[0]}.{line_split[10]} = {ind_happiness[f'{line_split[0]}.{line_split[10]}']}")

people.add("Me")


# Permutation Time Babay
next_perm = permutations(people)

for i in next_perm:
    for j in range(len(i)):
        try:
            current_happiness += ind_happiness[f'{i[j]}.{i[j+1]}']
            current_happiness += ind_happiness[f'{i[j+1]}.{i[j]}']
            #print(f'{i[j]}.{i[j+1]}')
        except IndexError:
            current_happiness += ind_happiness[f'{i[len(i) - 1]}.{i[0]}']
            current_happiness += ind_happiness[f'{i[0]}.{i[len(i) - 1]}']
            #print(f'{i[len(i) - 1]}.{i[0]}')
        #print(current_happiness)
    max_happiness = max(max_happiness, current_happiness)
    current_happiness = 0

print(max_happiness)
    