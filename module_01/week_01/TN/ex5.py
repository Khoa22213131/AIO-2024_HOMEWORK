import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TL.ex2 import elu as calc_elu

if __name__ == '__main__':
    print(round(calc_elu(-1, alpha=0.01), 2))