import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TL.ex4 import sinh as approx_sinh

if __name__ == '__main__':
    print(round(approx_sinh(x=3.14, n=10), 2))