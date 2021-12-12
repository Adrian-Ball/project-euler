#Project Euler Question 6

# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is 2640
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

max_num = 100

square_of_sum = (max_num * (max_num + 1) / 2) ** 2

# Nice proof here:
# See the graphical proof
# https://www.themathdoctors.org/summing-squares-finding-or-proving-a-formula/
sum_of_squares = max_num * (max_num + 1) * (max_num + 0.5) / 3

print(int(square_of_sum - sum_of_squares))