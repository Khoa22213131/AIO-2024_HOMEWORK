import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TL.ex4 import cosh as approx_cosh

if __name__ == '__main__':
    print(round(approx_cosh(x=3.14, n=10), 2))