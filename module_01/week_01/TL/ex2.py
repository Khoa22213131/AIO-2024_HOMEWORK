#Viết function mô phỏng theo 3 activation function.

import math

def sigmoid(x) :
    return 1 / (1 + math.exp(-x))

def relu(x) :
    return max(0, x)

def elu(x, alpha = 0.01) :
    if x >= 0 :
        return x
    else :
        return alpha * (math.exp(x) - 1)
    