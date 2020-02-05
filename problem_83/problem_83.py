from numpy import genfromtxt
import numpy as np

matrix_data = genfromtxt('p083_matrix.txt', delimiter=',')

print(matrix_data.shape)
