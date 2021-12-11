#Project Euler Question 5

# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

import sys
sys.path.append('../utility_functions')
from prime_functions import eratosthenes
import numpy as np

upper_lim = 20
primes = eratosthenes(upper_lim)
prime_powers = np.zeros(primes.shape)

for count in range(1,upper_lim+1):
    #Determine prime powers for current number
    n = count
    current_powers = np.zeros(primes.shape)
    for idx, prime in enumerate(primes):
        while n % prime == 0:
            current_powers[idx] += 1
            n = n / prime

    #Check and update final powers array
    for idx, power in enumerate(current_powers):
        if power > prime_powers[idx]:
            prime_powers[idx] = power

#Calculate answer
answer = 1
for prime, power in zip(primes, prime_powers):
    answer *= prime ** power
print(int(answer))