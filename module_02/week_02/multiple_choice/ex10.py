import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from exercise.part_1.e import inverse_matrix

m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)
