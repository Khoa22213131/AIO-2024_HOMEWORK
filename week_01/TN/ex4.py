import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TL.ex2 import sigmoid as calc_sig

if __name__ == '__main__':
    print(round(calc_sig(2), 2))