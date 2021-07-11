#Project Euler Question 199

# Three circles of equal radius are placed inside a larger circle 
# such that each pair of circles is tangent to one another and the 
# inner circles do not overlap. There are four uncovered "gaps" which 
# are to be filled iteratively with more tangent circles.

# At each iteration, a maximally sized circle is placed in each gap, 
# which creates more gaps for the next iteration. After 3 iterations, 
# there are 108 gaps and the fraction of the area which is not covered 
# by circles is 0.06790342, rounded to eight decimal places.

# What fraction of the area is not covered by circles after 10 iterations?
# Give your answer rounded to eight decimal places using the format x.xxxxxxxx .

import numpy as np

def recursive_get_apollonian_k(k1,k2,k3,curr_depth,final_depth):
    k0 = k1 + k2 + k3 + 2*np.sqrt(k1*k2 + k2*k3 + k1*k3)
    global k_arr
    k_arr = np.append(k_arr, k0)
    if curr_depth < final_depth:
        curr_depth += 1
        new_k = recursive_get_apollonian_k(k0,k1,k2,curr_depth,final_depth)
        new_k = recursive_get_apollonian_k(k0,k1,k3,curr_depth,final_depth)
        new_k = recursive_get_apollonian_k(k0,k2,k3,curr_depth,final_depth)

# k0 = k1 + k2 + k3 -/+ 2*np.sqrt(k1*k2 + k2*k3 + k1*k3)
k1 = k2  = k3 = 1
outer = k1 + k2 + k3 - 2*np.sqrt(k1*k2 + k2*k3 + k1*k3)
r0 = - 1 / outer

k_arr = np.array([1,1,1])

for i in range(3):
    recursive_get_apollonian_k(1,1,outer,1,10)
recursive_get_apollonian_k(1,1,1,1,10)

orig_area = np.pi * r0**2
k_to_area = lambda x: np.pi * (1/x)**2
taken_area = k_to_area(k_arr)
taken_area = np.sum(taken_area)

spare = 1 - (taken_area) / orig_area
print(f"Spare area as percentage: {spare:0.8f}")