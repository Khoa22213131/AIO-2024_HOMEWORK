import math

def sigmoid(x) :
    return 1 / (1 + math.exp(-x))

def relu(x) :
    return max(0, x)

def elu(x) :
    alpha = 0.01
    if x >= 0 :
        return x
    else :
        return alpha * (math.exp(x) - 1)
    
def calc_activation_func(x, act_name):
    if act_name == 'sigmoid' :
        return sigmoid(x)
    elif act_name == 'relu' :
        return relu(x)
    elif act_name == 'elu' :
        return elu(x)

print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))