#Project Euler Question 67

#By starting at the top of the triangle below and moving to adjacent numbers 
#on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt, 
# a 15K text file containing a triangle with one-hundred rows.

file_path = '../../../data/project-euler/p067_triangle.txt'
with open(file_path) as file:
    #Treat the first line as a special case, no predecessors
    prev_row = list(map(int, str.split(file.readline())))
    for line in file:
            curr_row = list(map(int, str.split(line)))
            curr_row[0] += prev_row[0]
            curr_row[-1] += prev_row[-1]
            #Determine the larger of the two parent elements
            #and then add to current element. 
            for element in range(1, len(curr_row)-1):
                max_prev = max(prev_row[element-1],prev_row[element])
                curr_row[element] += int(max_prev)
            prev_row = curr_row
            
answer = max(prev_row)
print(answer)
