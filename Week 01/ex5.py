import math

alpha = 0.01
def calc_elu ( x ) :
    if x >= 0 :
        return x
    else :
        return alpha * (math.exp(x) - 1)
    
print ( round ( calc_elu ( -1) , 2) )