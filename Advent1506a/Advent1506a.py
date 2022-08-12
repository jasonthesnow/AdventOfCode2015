puzzle_file = open('input.txt', 'r')

puzzle_input = puzzle_file.readlines()

puzzle_file.close()

corner_one = [0,0]
corner_two = [0,0]

light_grid = {"0.0": False}

lights_on = 0
lights_off = 0

for line in puzzle_input:

    puzzle_split = line.split()

    for i in range(len(puzzle_split)):
        try:
            

        except ValueError:
            pass
    
    
    
    #see if we are turning on or off lights

    try:
        x = line.index("turn on")
        print(f'Turn On Lights {corner_one[1]},{corner_one[1]} to {corner_two[0]},{corner_two[1]}')
    except ValueError:
        pass

    try:
        x = line.index("turn off")
        print(f'Turn Off Lights {corner_one[1]},{corner_one[1]} to {corner_two[0]},{corner_two[1]}')
    except ValueError:
        pass

    try:
        x = line.index("toggle")
        print(f'Toggle Lights {corner_one[1]},{corner_one[1]} to {corner_two[0]},{corner_two[1]}')
    except ValueError:
        pass
    