puzzle_file = open("input.txt", "r")
puzzle_input = puzzle_file.readlines()
puzzle_file.close()

puzzle_file_test = open('input_test.txt.', 'r')
puzzle_input_test = puzzle_file_test.readlines()
puzzle_file_test.close()

wire = {"": 0}
shift_count = 0

undefined_wire = 1

has_operation = False # Tests to see if there's an operation or if it's a given value

count = 0


####TO DO LIST####

# 1. Find out which gate is happening (AND/OR/RSHIFT etc.)
# 2. Import all given numbers and start from there
# 3. Go through and start defining each wire with the given information
# 4. Loop until all wires are defined
# 5. Print out wire A

while not undefined_wire == 0:
    count = 0
    undefined_wire = 0
    for line in puzzle_input:

        count = count + 1
        #print(f'{count}: {line.strip()}')


        # AND FUNCTION
        try:
            x = line.index('AND')
            has_operation = True
            #print('AND')

            try:
                placer = line.split()
                try:
                    wire[placer[4]] = int(placer[0]) & wire[placer[2]]
                except ValueError:
                    try:
                        wire[placer[4]] = wire[placer[0]] & int(placer[2])
                    except ValueError:
                        wire[placer[4]] = wire[placer[0]] & wire[placer[2]]

                #print(f'Wire {placer[4]} = {wire[placer[4]]}')

            except KeyError:
                #print('One or more wires not defined yet')
                has_passed = True
                undefined_wire = undefined_wire + 1

        except ValueError:
            pass

    
        # OR FUNCTION
        try:
            x = line.index('OR')
            has_operation = True
            #print('OR')

            try:
                placer = line.split()

                try:
                    wire[placer[4]] = int(placer[0]) | wire[placer[2]]
                except ValueError:
                    try:
                        wire[placer[4]] = wire[placer[0]] | int(placer[2])
                    except ValueError:
                        wire[placer[4]] = wire[placer[0]] | wire[placer[2]]

                #print(f'Wire {placer[4]} = {wire[placer[4]]}')


            except KeyError:
                #print('One or more wires not defined yet')
                undefined_wire = undefined_wire + 1

        except ValueError:
            pass

    
        #RSHIFT FUNCTION
        try:
            x = line.index('RSHIFT')
            has_operation = True
            placer = line.split()
            shift_count = int(placer[2])
            #print(f'RSHIFT {shift_count}')

            try:
                placer = line.split()

                wire[placer[4]] = wire[placer[0]] >> int(placer[2])

                #print(f'Wire {placer[4]} = {wire[placer[4]]}')


            except KeyError:
                #print('One or more wires not defined yet')
                undefined_wire = undefined_wire + 1

        except ValueError:
            pass


        #LSHIFT FUNCTION
        try:
            x = line.index('LSHIFT')
            has_operation = True
            placer = line.split()
            shift_count = int(placer[2])
            #print(f'LSHIFT {shift_count}')

            try:
                placer = line.split()


                wire[placer[4]] = wire[placer[0]] << int(placer[2])

                #print(f'Wire {placer[4]} = {wire[placer[4]]}')


            except KeyError:
                #print('One or more wires not defined yet')
                undefined_wire = undefined_wire + 1

        except ValueError:
            pass


        #NOT FUNCTION
        try:
            x = line.index('NOT')
            has_operation = True
            #print('NOT')

            try:
                placer = line.split()

                try:
                    wire[placer[3]] = 65535 ^ int(wire[placer[1]])
                except ValueError:
                    wire[placer[3]] = 65535 ^ wire[placer[1]]

                #print(f'Wire {placer[3]} = {wire[placer[3]]}')


            except KeyError:
                #print('One or more wires not defined yet')
                undefined_wire = undefined_wire + 1

        except ValueError:
            pass

        #NO FUNCTION
        if not has_operation:
            placer = line.split()
            try:
                wire[placer[len(placer) - 1]] = int(placer[0])

                #print(f'{placer[len(placer) - 1]} is equal to {placer[0]}')
            except ValueError:
                try:
                    wire[placer[len(placer) - 1]] = wire[placer[0]]
                except KeyError:
                    undefined_wire = undefined_wire + 1



    
        has_operation = False


    #print(wire)

    print(f'There are still {undefined_wire} undefined wires')

    try:
        print(f"Wire A is: {wire['a']}")
    except KeyError:
        pass

        
