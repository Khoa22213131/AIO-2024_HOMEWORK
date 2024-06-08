import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TL.ex4 import sin as approx_sin

if __name__ == '__main__':
    print(round(approx_sin(x=3.14, n=10), 4))