import math

#This number has been entered and confirmed to be too big
#known_big_number = 818000



puzzle_input = 1500

current_gifts = 0
current_house_number = 0
# last_house_number = 0

# A surprisingly not simple problem. Optimize

### WAYS TO OPTIMIZE ###
# 1. Only test up to half the number (anythine above half of the number will never be divisible)
# 2. Only test non prime numbers
#     - Note: only works if finding the prime number is less demanding than finding remainders
# 3. Find more ways to quickly determine if a number isn't divisible by other numbers
#   a. Have multiplicity rules? 
#       i. Convert number to string
#      ii. Test if even. If not even can rule out all even numbers.
#     iii. Test if divisible by 3. Can remove all multiples of 3
#      iv. Test if divisible by 5. Can remove all multiples of 5

while True:
    current_house_number += 1
    
    for j in range(math.floor(current_house_number / 2)):
        if current_house_number % (j + 1) == 0:
            current_gifts += ((j + 1) * 10)
    current_gifts += current_house_number * 10
    
    print(f'House {current_house_number}: {current_gifts} gifts')

    if not (current_gifts < puzzle_input):
        print(current_house_number)
        break 
    else:
        current_gifts = 0
        # last_house_number = current_house_number