import math
import time

#This number has been entered and confirmed to be too big
#known_big_number = 818000
start_time = time.time()

prime_numbers = [2]

puzzle_input = 34000000

current_gifts = 0
current_house = 0
# last_house_number = 0

# A surprisingly not simple problem. Optimize

### WAYS TO OPTIMIZE ###
# 1. Only test up to half the number (anythine above half of the number will never be divisible)
# 2. Only test non prime numbers
#     - Note: only works if finding the prime number is less demanding than finding remainders
#     - With my new way, I have to find the prime numbers anyways, so that should be easy
# 3. Find more ways to quickly determine if a number isn't divisible by other numbers
#   a. if we can prove a prime number isn't a prime, we can rule out a lot of numbers to try
#       i. for instance, if 2 isn't a factor, we can rule out all even numbers

def multiplicity_prime(n, p):
    # P is prime number that is less than half the current number, N is the current number
    if n % p == 0:
        return True
    else:
        return False

def is_prime(n):
    prime = True
    for i in range(2, math.ceil(math.sqrt(n) + 1)):
        if n % i == 0:
            prime = False
    if prime:
        return True
    else:
        return False

for i in range(10000):
    current_house += 1

    if is_prime(current_house):
        #print(f'New Prime: {current_house}')
        prime_numbers.append(current_house)
        continue # No need to test any of these houses

    tested_numbers = set()
    if not current_house in prime_numbers:
        for j in range(len(prime_numbers)):
            if multiplicity_prime(current_house, prime_numbers[j]):
                for k in range(2, int(current_house / 2), prime_numbers[j]): # Instead of testing every number, only testing multiples of the primes that are factors
                    if not (k in tested_numbers): # Checks to make sure not testing similar numbers (for instance 6 would be in both 2 and 3)
                        tested_numbers.add(k)
                        if current_house % k == 0:
                            current_gifts += 10 * k

    current_gifts += (current_house * 10) + 10

    # print(f'House {current_house}: {current_gifts} gifts')
    

    if not (current_gifts < puzzle_input):
        print(current_house)
        break
    else:
        current_gifts = 0

print(time.time() - start_time)