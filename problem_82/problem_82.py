from numpy import genfromtxt
import numpy as np

matrix_data = genfromtxt('p082_matrix.txt', delimiter=',')
traversal_cost = matrix_data[:,0,np.newaxis]
#traversal_cost = traversal_cost[:, np.newaxis]

for col in range(1,matrix_data.shape[1]):
    
    right_col = matrix_data[:,col, np.newaxis]
    
    #Travelling straight (from left to right)
    trav_right = np.add(traversal_cost,right_col)
    
    #Travelling right then down 
    trav_right_down = np.empty([matrix_data.shape[0],1])
    for elem in range(0,matrix_data.shape[0]):
        if elem == 0:
            trav_right_down[elem] = traversal_cost[elem] + right_col[elem]
        else:
            cost = trav_right_down[elem-1] + right_col[elem]
            trav_right_down[elem] = min(cost, trav_right[elem,0])

    #Travelling right then up 
    trav_right_up = np.empty([matrix_data.shape[0],1])
    for elem in range(matrix_data.shape[0]-1,-1,-1):
        if elem == matrix_data.shape[0]-1:
            trav_right_up[elem] = traversal_cost[elem] + right_col[elem]
        else:
            cost = trav_right_up[elem+1] + right_col[elem]
            trav_right_up[elem] = min(cost, trav_right[elem,0])

    curr_costs = np.concatenate((trav_right,trav_right_down,trav_right_up),axis=1)
    traversal_cost = np.min(curr_costs, axis=1)
    traversal_cost = traversal_cost[:, np.newaxis]

#Get the cheapest path cost
print(min(traversal_cost))