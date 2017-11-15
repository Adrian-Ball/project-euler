#Project Euler Question 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

import sys
sys.path.append('../utility_functions')


#We will want to make use of the arithmetic sum here
from arithmetic_sum import arithmetic_sum

n = 999; 

answer = arithmetic_sum(3,(n//3)*3,n//3)   \
         + arithmetic_sum(5,(n//5)*5,n//5) \
         - arithmetic_sum(15,(n//15)*15,n//15)

#Answer should be an int as we are summing integers
print('The answer is:',int(answer))