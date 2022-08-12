from asyncio import WindowsProactorEventLoopPolicy


total_area = 0;

puzzle_input = open('input.txt', 'r')

Lines = puzzle_input.readlines()

count = 0
ribbon = 0

for line in Lines:
    # print(line.strip().split('x'))

    w = int(line.strip().split('x')[0])
    l = int(line.strip().split('x')[1])
    h = int(line.strip().split('x')[2])

    side1 = 2*w*l
    side2 = 2*w*h
    side3 = 2*h*l

    small_side = (min([side1, side2, side3])) / 2
    
    total_area += side1 + side2 + side3 + small_side

    count += 1

    # Amount of wrapping paper needed

    # print(str(count) + ": " + str(total_area))


    # figure out amount of ribbon needed

    ribbon += min([(2*w + 2*l), (2*w + 2*h), (2*l + 2*h)])
    ribbon += w*l*h

    print(ribbon)



