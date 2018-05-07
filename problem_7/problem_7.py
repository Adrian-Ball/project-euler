#Project Euler Question 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import sys
sys.path.append('../utility_functions')
from prime_functions import eratosthenes

nth_prime = 10001
pow = 5
#Being a little lazy here, and just going to call prime function until 
#we have the required amount. 
while True:
    max_num = 2**pow
    primes = eratosthenes(max_num)
    if len(primes) >= nth_prime:
        answer = primes[nth_prime-1]
        break
    else:
        pow += 1

print(answer)