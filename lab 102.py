import numpy as np

arbitrary_a_b = np.array([1.5,5.0])
data_table = np.array([[2.2,6.14],
               [1.3,4.72],
               [4.2,11.17],
               [5.8,14.23],
               [3.4,9.55],
               [8.7,22.49]]) 
train_x = data_table[:, 0]
train_y = data_table[:, 1]

mse =sum(((arbitrary_a_b[0] * train_x + arbitrary_a_b[1])-train_y)**2)/4
print("The MSE:", mse)