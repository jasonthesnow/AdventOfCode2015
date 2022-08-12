puzzle_file = open('input.txt', 'r')
puzzle_input = puzzle_file.readlines()
puzzle_file.close()

raw_length = 0

encode_length = 0

total_encode_length = 0

for i in range(len(puzzle_input)):
    
    raw_length = len(puzzle_input[i].strip())
    
    for j in range(len(puzzle_input[i])):
        if puzzle_input[i][j] == '"':
            if j == 0 or j == (len(puzzle_input[i].strip()) - 1): # testing if it's the opening or closing ""
                encode_length += 2
            else: # if it's not the opening or closing quotes, it only needs to add a slash if it's in the middle of the string
                encode_length += 1

        if puzzle_input[i][j] == '\\':
            encode_length += 1

print(encode_length)