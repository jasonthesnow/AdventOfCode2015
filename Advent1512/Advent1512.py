puzzle_file = open('input.txt','r')
puzzle_input = puzzle_file.readline()
puzzle_file.close()

x = 0

total = 0

def checkNumber(char):
    if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0":
        return True
    else:
        return False


for i in range(len(puzzle_input)):
    temp_string = ""
    isNumber = False
    try:
        while checkNumber(puzzle_input[i + x]):
            temp_string += puzzle_input[i + x]
            x += 1
            isNumber = True

        if puzzle_input[i + x - len(temp_string) - 1] == "-":
            total -= int(temp_string)
            print(f'Current number is -{temp_string}. New total is {total}')
        else:
            total += int(temp_string)
            print(f'Current number is {temp_string}. New total is {total}')
    
    except:
        pass