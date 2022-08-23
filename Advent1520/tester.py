# Testing how long certain functions take to find the most optimized way of running the code

# Basically I'm slowly adding more functions and tests and if it's slower than the old way, I take it out. If it's faster I keep it in.
# I will keep doing this until I find the fastest possible way to test 10k houses

import time
import math

primes = list()
start_time = time.time()
current_house = 0
current_gifts = 0
num_of_calculations = 0

def is_prime(n):
    prime = True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            prime = False
            break
    if prime and (not n == 1):
        return True
    else:
        return False

for i in range(10000):
    current_house += 1
    tested = set()

    if not (is_prime(current_house)):
        for j in range(len(primes)):
            num_of_calculations += 1
            if current_house % primes[j] == 0:
                for k in range(1, int(current_house / primes[j])):
                    num_of_calculations += 1
                    if current_house % (primes[j] * k) == 0 and (not primes[j] * k in tested):
                        tested.add(primes[j] * k)
                        current_gifts += primes[j] * k * 10  
    else:
        primes.append(current_house)
    
    current_gifts += ((current_house) * 10) + 10

    #print(primes)
    print(f'House {current_house}: {current_gifts} Gifts')


    current_gifts = 0


print(num_of_calculations)
print(time.time() - start_time)