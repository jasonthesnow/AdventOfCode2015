READ ME

I'm documenting all of my optimizations for Advent1520 in here and my though processes


Every for loop listed below lives in this if statement:

  if not is_prime(current_house):
    #stuff happens
  else:
    primes.append(current_house)
    
Where is_prime looks like the following:

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



I'm calculating the number of times the % operator is called (outside of the prime number function since that is a constant in all of the tests)

The most basic function test is as follows:

    for j in range(int(current_house)):
      if current_house % (j + 1) == 0:
        current_gifts += (j + 1) * 10
   
In a loop of 10000, the % operator is called 44,268,604 times, and takes on average about 3.1 seconds to run.


The first optimization is to half the for loop's number of tests, looking like this:

    for j in range(int(current_house / 2)):
      if current_house % (j + 1) == 0:
        current_gifts += (j + 1) * 10
    current_gifts += current_house * 10
        
Because any number above half of the original house number will not be a factor. This optimization only calls the % operator 22,132,416 and takes on average about 1.5 seconds to run.


Taking the above line of thinking further, we know that if a number is not divisible by 2 or 3, any numbers above 1/3 of the original will not be factors. going further, a number's largest factor will be smaller than 1/(the lowest prime factor).

This is where my math fails me, however. My original thought was to only check prime numbers, looking like this:

    for j in range(len(primes)):
      if current_house % prime[j] == 0:
        current_gifts += primes[j] * 10
        
Where primes was a list of all prime numbers up to the current house number

This leaves out many possible factors, however (for instance, house 12 would only check 2 and 3, and not 4 or 6).



My next thought was to check only multiples of factors looking like this:

    for j in range(len(primes)):
        if current_house % primes[j] == 0:
          for k in range(1, int(current_house / primes[j]) + 1, primes[j]):
            if current_house % (primes[j] * k) == 0:
              current_gifts += primes[j] * k * 10
              
This left in multiple repeated numbers, however. Taking 12 as the example again, it would loop testing if 2, 4, 6... were factors, and then with three test 3, 6... as factors, meaning 6 would be added to current_gifts twice. This also potentially has other problems in the code.


To fix the repeat numbers, I added a set of numbers that had already been tested, looking like this:
  
  tested = set()
  for j in range(len(primes)):
    if current_house % primes[j] == 0:
      for k in range(1, int(current_house / primes[j])):
        if current_house % (primes[j] * k) == 0 and (not primes[j] * k in tested):
          tested.add(primes[j] * k)
          current_gifts += primes[j] * k * 10
          
This ran the slowest of all, though, taking almost 3.5 seconds on average to test 10,000 houses, and took 28,390,808 % operations.



So far the fastest code to run is simply testing every number between 1 and half the current house number. I believe there is an optimization to be made only testing prime factors but my brain is bleeding and I cannot find the solution. I will continue working on this when I have time
















              
