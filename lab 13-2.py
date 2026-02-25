import numpy as np
fvalues = [89, 102 , 89.45, 68.23 ,56.89, 90.6, 45.3, 67.9 , 88.05, 50.2]
F = np.array(fvalues)
C = (F-32) * 5/9
print("Farenheit: ", F)
print("Converted to Celcius: ",C)



