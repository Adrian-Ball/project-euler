import csv

#Get the data
matrix_file = open('p081_matrix.txt','r')
reader = csv.reader(matrix_file)
progress_row = []

for row in reader:
    row = list(map(int, row))

    #If its the first roc
    if not progress_row:
        progress_row = row
        for elem in range(1,len(row)):
            progress_row[elem] += progress_row[elem-1]
    #For every other row
    else:
        for elem in range(len(row)):
            if elem == 0:
                progress_row[elem] += row[elem]
            else:
                progress_row[elem] = min(progress_row[elem],progress_row[elem-1]) + row[elem]

print(progress_row[-1])