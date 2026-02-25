import numpy as np
A = np.array ([[1,2,3],
               [4,5,6],
               [7,8,9]])

B = np.array ([[9,8,7],
               [6,5,4],
               [3,2,1]])
calculated_matrix1 = (A**2)+2*B
calculated_matrix_part1 =(A + B).T 
calculated_matrix_part2 = (A-B)
total_calculationparts = np.dot(calculated_matrix_part1 , calculated_matrix_part2)
print("Matrix 1: \n", calculated_matrix1)
print("Matrix 2:\n",total_calculationparts)