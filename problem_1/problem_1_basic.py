#Project Euler Question 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#In this version of the solution we simply iterate over all the numbers to
#check whether they meet the divisibility criteria

n = 1000; 
#Initialise the answer
answer = 0;

for count in range(1,n):
    if count%3 == 0 or count%5 == 0:
        answer = answer + count
        
print('The answer is:',answer)

