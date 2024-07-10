import numpy as np

arr1 = np.ones((3, 3)) > 0
arr2 = np.ones((3, 3), dtype=bool)
arr3 = np.full((3, 3), fill_value=True, dtype=bool)

print('a) : ', arr1)
print('b) : ', arr2)
print('c) : ', arr3)
