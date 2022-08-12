text_file = open('input.txt')

puzzle_input = text_file.read();

text_file.close()

row = 0
col = 0

robo_row = 0
robo_col = 0

presents = 1

houses = {str(col) + "." + str(col): True}

real_santa = True

for i in range (0, len(puzzle_input)):
    if real_santa:
        if puzzle_input[i] == '^':
            row += 1
        elif puzzle_input[i] == 'v':
            row -= 1
        elif puzzle_input[i] == '<':
            col -= 1
        elif puzzle_input[i] == '>':
            col += 1

        try:
            if houses[str(col) + "." + str(row)]:
               print("House " + str(col) + "." + str(row) + " already has a present! House visted by Real Santa. Houses Visited: " + str(presents))
            else:
                print("oh now. it's broken. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        except:
            houses[str(col) + "." + str(row)] = True
            presents += 1
            print("New House " + str(col) + "." + str(row) + " visited! House visted by Real Santa. Houses Visited: " + str(presents))
        
        real_santa = False
    else:
        if puzzle_input[i] == '^':
            robo_row += 1
        elif puzzle_input[i] == 'v':
            robo_row -= 1
        elif puzzle_input[i] == '<':
            robo_col -= 1
        elif puzzle_input[i] == '>':
            robo_col += 1
    
        try:
            if houses[str(robo_col) + "." + str(robo_row)]:
               print("House " + str(robo_col) + "." + str(robo_row) + " already has a present! House visted Robot Santa. Houses Visited: " + str(presents))
            else:
               print("oh now. it's broken. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        except:
            houses[str(robo_col) + "." + str(robo_row)] = True
            presents += 1
            print("New House " + str(robo_col) + "." + str(robo_row) + " visited! House visted by Robot Santa. Houses Visited: " + str(presents))
        
        real_santa = True

print("Total amount of Houses Visited: " + str(presents))