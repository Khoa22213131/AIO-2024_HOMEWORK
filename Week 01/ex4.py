import math

def calc_sig ( x ) :
    return 1 / (1 + math.exp(-x))
    
    
print(round(calc_sig(2), 2))