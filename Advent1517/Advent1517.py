from itertools import combinations
puzzle_input = 'input.txt'
total_eggnog = 150

possible_combo = 0
current_capacity = 0
containers = list()
min_containers = False

with open(puzzle_input) as f:
    for line in f:
        containers.append(int(line))

for i in range(len(containers)):
    perm = combinations(containers, i + 1)
    for j in perm:
        if sum(j) == total_eggnog:
            possible_combo += 1
            min_containers = True

    if min_containers:
        break
    

print(possible_combo)
