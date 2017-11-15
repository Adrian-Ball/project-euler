#Project Euler Question 85

#By counting carefully it can be seen that a rectangular grid measuring 
#3 by 2 contains eighteen rectangles.
#Although there exists no rectangular grid that contains exactly two million 
#rectangles, find the area of the grid with the nearest solution.

import sys
sys.path.append('../utility_functions')

#We will want to make use of the arithmetic sum here
from arithmetic_sum import arithmetic_sum
import math

answer = 0
distance_to_2mil = 2000000

limit_i = math.ceil(math.sqrt(2000000))
for i in range(1,limit_i):
    limit_j = round(2000000/i)
    for j in range(1,limit_j):
        term_1 = arithmetic_sum(1,i,i)
        term_2 = arithmetic_sum(1,j,j)
        num_rectangles = term_1 * term_2
        if abs(num_rectangles - 2000000) < distance_to_2mil:
            distance_to_2mil = abs(num_rectangles - 2000000)
            answer = i*j
        
print('The answer is:',answer)