import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TL.ex4 import cos as approx_cos

if __name__ == '__main__':
    print(round(approx_cos(x=3.14, n=10), 2))