import time

start_time = time.time()

puzzle_input = 34000000
current_house = 500000
current_gifts = 0

while True:
    current_house += 1

    for j in range(int(current_house / 2)):
        if current_house % (j + 1) == 0:
            current_gifts += (j + 1) * 10
    
    current_gifts += (current_house * 10)
    
    print(f'House {current_house}: {current_gifts} gifts')

    if not (current_gifts < puzzle_input):
        print(current_house)
        break
    else:
        current_gifts = 0

print(time.time() - start_time)



#786240 is THE NUMBER AND IT TOOK 10 MINUTES TO SOLVE
#818000 is too high