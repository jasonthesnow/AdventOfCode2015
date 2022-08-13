##ONLY SOLVES PART 1

puzzle_input = "input.txt"
steps = 100

#{Row #, {Col #, "information"}}

line_num = 0
lights = dict()
lights_on = 0

with open(puzzle_input) as f:
    for line in f:
        lights[line_num] = {}
        for i  in range(len(line.strip())):
            lights[line_num][i] = line[i]
            #print(f'Line {line_num} Character {i}: {lights[line_num][i]}')
        #print(f'{line_num} {lights[line_num]}')

        line_num += 1

#print("")
# Conway's Game of Life

for s in range(steps):
    new_lights = dict()
    for i in range(len(lights)):
        new_lights[i] = {}
        for j in range(len(lights[i])):
            try:
                if lights[i - 1][j - 1] == "#": lights_on += 1
            except KeyError:
                pass

            try:
                if lights[i - 1][j] == "#": lights_on += 1
            except KeyError:
                pass

            try:
                if lights[i - 1][j + 1] == "#": lights_on += 1
            except KeyError:
                pass

            try:
                if lights[i][j - 1] == "#": lights_on += 1
            except KeyError:
                pass

            try:
                if lights[i][j + 1] == "#": lights_on += 1
            except KeyError:
                pass

            try:
                if lights[i + 1][j - 1] == "#": lights_on += 1
            except KeyError:
                pass

            try:
                if lights[i + 1][j] == "#": lights_on += 1
            except KeyError:
                pass

            try:
                if lights[i + 1][j + 1] == "#": lights_on += 1
            except KeyError:
                pass

            #print(lights_on)

            if lights[i][j] == "#":
                if not (lights_on == 2 or lights_on == 3):
                    new_lights[i][j] = "."
                else:
                    new_lights[i][j] = "#"
            elif lights[i][j] == ".":
                if lights_on == 3:
                    new_lights[i][j] = "#"
                else:
                    new_lights[i][j] = "."

            lights_on = 0
        #print(f'{i} {new_lights[i]}')

    lights = new_lights
    #print("")

for i in range(len(lights)):
    for j in range(len(lights[i])):
        if lights[i][j] == "#": lights_on += 1

print(lights_on)