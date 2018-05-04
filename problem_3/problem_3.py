#Project Euler Question 3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import sys
sys.path.append('../utility_functions')
import math
from prime_functions import eratosthenes

#Answer cant be larger than the sqrt of the number
upper_lim = math.ceil(600851475143**0.5)
potential_primes = eratosthenes(upper_lim)
#Count down as we want to find largest prime
for counter in range(len(potential_primes)-1, 0, -1):
    if 600851475143 % potential_primes[counter] == 0:
        answer = potential_primes[counter]
        break

print(answer)