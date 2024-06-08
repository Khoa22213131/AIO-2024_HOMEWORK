import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from TL.ex1 import max_kernel

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

if __name__ == "__main__":
    print(max_kernel(num_list, k))
