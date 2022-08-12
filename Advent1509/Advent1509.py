from itertools import permutations
from sys import maxsize

puzzle_file = open('input.txt','r')
puzzle_input = puzzle_file.readlines()
puzzle_file.close()

min_dist = maxsize
max_dist = 0
current_dist = 0

location = set()
distance = dict()

for i in range(len(puzzle_input)):
    line  = puzzle_input[i].split()
    location.add(line[0])
    location.add(line[2])
    
    distance[f'{line[0]}.{line[2]}'] = int(line[4])
    distance[f'{line[2]}.{line[0]}'] = int(line[4])


next_perm = permutations(location)
count = 1

for i in next_perm:
    print(f'Trip {count}')
    for j in range(len(i) - 1):
        
        current_dist += distance[f'{i[j]}.{i[j+1]}']
        
        print(f'{i[j]} -> {i[j+1]}')
        
    count += 1
    print(f'Total Distance: {current_dist}')
    min_dist = min(min_dist, current_dist)
    max_dist = max(max_dist, current_dist)
    current_dist = 0
    print("")

print("")
print(f'Shortest Distance: {min_dist}')
print(f'Longest Distance: {max_dist}')