#A (growing) collection of functions for finding prime numbers

import numpy as np 
import math

#Sieve of Eratosthenes
#Find all prime numbers up to and including num
def eratosthenes (num):
    #All numbers to check
    sieve_numbers = np.ones(num)
    sieve_numbers[0] = 0
    counter_limit = math.ceil(num**0.5)+1
    for counter in range(1,counter_limit):
        #If hasnt been identified as prime yet
        if sieve_numbers[counter] == 1:
            next_val = counter+counter+1

            while True:
                if next_val >= num:
                    break
                else:
                    sieve_numbers[next_val] = 0
                    next_val += counter+1
    primes = np.add(np.nonzero(sieve_numbers),1)
    return primes[0]

