import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from exercise.part_1.a import compute_vector_length

vector = np.array([-2, 4, 9, 21])
result = compute_vector_length([vector])
print(round(result, 2))
