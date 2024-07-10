import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5) & (a <= 10))
print("result", a[index])
