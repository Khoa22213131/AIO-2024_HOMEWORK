import numpy as np

arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
print(arr)
