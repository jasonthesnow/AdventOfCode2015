puzzle_input = "1321131112"
temp_input = ""
iteration = 50
count = 1

print(f'Start: Current string is: {puzzle_input}')

for i in range(iteration):
    for j in range(len(puzzle_input)):
        try:
            if puzzle_input[j] == puzzle_input[j + 1]:
                count += 1
            else:
                temp_input += str(count) + puzzle_input[j]
                #print(temp_input)
                count = 1
        except IndexError:
            temp_input += str(count) + puzzle_input[j]
            #print(temp_input)
            count = 1
    
    puzzle_input = temp_input
    temp_input = ""

    #print(f'Iteration {i + 1}: Current string is: {puzzle_input}')

print(len(puzzle_input))
