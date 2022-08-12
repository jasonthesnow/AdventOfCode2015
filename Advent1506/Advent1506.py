#Open puzzle input, read it Line by line, close file

puzzle_input = open('input.txt', 'r')

Lines = puzzle_input.readlines()

puzzle_input.close()



#Declare variables

light_x = 0;
light_y = 0;

light_dict = {str(light_x) + "." + str(light_y): 0} #Dictionary holding all coordinates and if the light is on or off (true being on, false being off)

count = 1 #Which line number I am on

light_bright = 0



for line in Lines: # Go line by line, turning off and on the lights asked for

    is_first_int = True #I'm bad at coding, basic toggle

    coord_one = ['x1', 'y1']
    coord_two = ['x2', 'y2']


    # Find the coordinates in the instruction, splitting by white space and searching each chunk for a comma (only the coordinates have a comma in each line)

    broken = line.split()

    for i in range(len(broken)): #searching each word for a comma
        try:
            x = broken[i].index(",") #if the word has a comma, it must be a coordinate set
            coord_string = broken[i].split(",") #split word up into the two numbered coordinates

            if is_first_int:
                coord_one[0] = coord_string[0]
                coord_one[1] = coord_string[1]
                is_first_int = False
            else:
                coord_two[0] = coord_string[0]
                coord_two[1] = coord_string[1]
                is_first_int = True
            
            print(coord_string) #sanity check print to visually verify all coordinates are correct

        except ValueError:
            pass

                
    print(f'Corner one is {coord_one[0]},{coord_one[1]} and Corner Two is {coord_two[0]},{coord_two[1]}') #sanity check print to visually verify all coordinates are correct


    try:
        x = line.index("turn off") #test to see if we are turning off lights

        for i in range(int(coord_one[0]), int(coord_two[0]) + 1): # going row by row from the first x coordinate to the last x coordinate
            for j in range(int(coord_one[1]), int(coord_two[1]) + 1):# going across the row for each y coordinate
               try: 
                   if light_dict[f'{i},{j}'] > 0:
                       light_dict[f'{i},{j}'] = light_dict[f'{i},{j}'] - 1 # subtracting 1 from each light
               except:
                   pass


        print(str(count) + ": turn off" )
    except ValueError:
        pass

    try:
        x = line.index("turn on")

        for i in range(int(coord_one[0]), int(coord_two[0]) + 1):
            for j in range(int(coord_one[1]), int(coord_two[1]) + 1):

               try: 
                   light_dict[f'{i},{j}'] = light_dict[f'{i},{j}'] + 1 # subtracting 1 from each light
               except:
                   light_dict[f'{i},{j}'] = 0
                   light_dict[f'{i},{j}'] = light_dict[f'{i},{j}'] + 1



        print(str(count) + ": turn on")
    except ValueError:
        pass

    try:
        x = line.index("toggle")

        for i in range(int(coord_one[0]), int(coord_two[0]) + 1):
            for j in range(int(coord_one[1]), int(coord_two[1]) + 1):

               try: 
                   light_dict[f'{i},{j}'] = light_dict[f'{i},{j}'] + 2 # subtracting 1 from each light
               except:
                   light_dict[f'{i},{j}'] = 0
                   light_dict[f'{i},{j}'] = light_dict[f'{i},{j}'] + 2


        print(str(count) + ": toggle")
    except ValueError:
        pass

    count += 1



#Tally up amount of lights that are on and off

for i in range(1000):
    for j in range(1000):
        try:
            light_bright = light_bright + light_dict[f'{i},{j}']
        except KeyError:
            pass

            # Again, assuming all lights were off to begin with

    print("Row " + str(i) + " is counted")

print(f'The total brightness is {light_bright}')

#Sanity check at the end, making sure the amount of lights that are off and the amount of lights that are on equals 1,000,000


