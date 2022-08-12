floor_num = 0

puzzle_input = open('input.txt','r')

puzzle_input_string = puzzle_input.read()

# print(len(puzzle_input_string))

for i in range(0, len(puzzle_input_string)):
    if puzzle_input_string[i] == '(': 
        floor_num = floor_num + 1 
    elif puzzle_input_string[i] == ")": 
        floor_num = floor_num - 1

    if floor_num < 0:
        print(i)
        
