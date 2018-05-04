#Set answer to 0
largest_palindrome = 0

#Quick test function for a number being palindromic
#Note only accurate for 3-7 digit numbers
#Input numbers only range from 5-6 digits
def is_palindrome(num):
    num_as_str = str(num)
    is_pal = True
    for count in range(0,3):
        if num_as_str[count] != num_as_str[-(count+1)]:
            is_pal = False
            break
    return is_pal

#Count one number from large to small, only want 3 digit numbers
for num1 in range(999,99,-1):
    num2 = 999
    #only need one number to iterate over everything, removes repeats
    while num2 >= num1:
        current_number = num1*num2
        if current_number < largest_palindrome:
            break
        if is_palindrome(current_number):
            largest_palindrome = current_number
        num2 -= 1

print(largest_palindrome)