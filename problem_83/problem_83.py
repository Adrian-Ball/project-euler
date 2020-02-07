#Project Euler Question 83

# Find the minimal path sum from the top left to the bottom 
# right by moving left, right, up, and down in matrix.txt

import numpy as np
from numpy import genfromtxt

#Define start and end locations
start_loc_row, start_loc_col = 0,0
goal_loc_row, goal_loc_col = -1,-1

#Load the data
matrix_data = genfromtxt('p083_matrix.txt', delimiter=',')
NUM_ROWS = matrix_data.shape[0]
NUM_COLS = matrix_data.shape[1]

####
#Some Initialization 
####
#Matrix same size as data that has the current path cost to each element, Inf if unvisited
sum_to_nodes = np.zeros((80,80)) + np.Infinity
sum_to_nodes[start_loc_row, start_loc_col] = matrix_data[start_loc_row, start_loc_col] 
#Potential branches to check on path
path_values_to_check = np.array((1,))
path_values_to_check[0] = matrix_data[start_loc_row, start_loc_col] 

#While the BFS has not reached the goal location
while sum_to_nodes[goal_loc_row, goal_loc_col] == np.Infinity:
    min_cost_elems = np.where(sum_to_nodes == path_values_to_check[0])
    min_cost_row =  min_cost_elems[0][0]
    min_cost_col = min_cost_elems[1][0]

    adjacent_nodes = np.zeros((4,2))
    #Up
    adjacent_nodes[0,0] = np.minimum(min_cost_row, (min_cost_row - 1) % NUM_ROWS)
    adjacent_nodes[0,1] = min_cost_col
    #Left
    adjacent_nodes[1,0] = min_cost_row 
    adjacent_nodes[1,1] = np.minimum(min_cost_col, (min_cost_col - 1) % NUM_COLS)
    #Down
    adjacent_nodes[2,0] = np.maximum(min_cost_row, (min_cost_row + 1) % NUM_ROWS)
    adjacent_nodes[2,1] = min_cost_col
    #Right
    adjacent_nodes[3,0] = min_cost_row 
    adjacent_nodes[3,1] = np.maximum(min_cost_col, (min_cost_col + 1) % NUM_COLS)
    adjacent_nodes = np.uint(adjacent_nodes)

    for count in range(0,4):
        if sum_to_nodes[adjacent_nodes[count,0],adjacent_nodes[count,1]] == np.Infinity:
            sum_to_nodes[adjacent_nodes[count,0],adjacent_nodes[count,1]] = matrix_data[adjacent_nodes[count,0],adjacent_nodes[count,1]] +\
                                                                            sum_to_nodes[min_cost_row, min_cost_col]
            path_values_to_check = np.append(path_values_to_check, sum_to_nodes[adjacent_nodes[count,0],adjacent_nodes[count,1]])
    path_values_to_check = np.delete(path_values_to_check, 0)
    path_values_to_check = np.sort(path_values_to_check)


print(int(sum_to_nodes[goal_loc_row, goal_loc_col]))
