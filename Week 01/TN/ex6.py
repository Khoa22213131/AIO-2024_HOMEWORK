import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TL.ex2 import sigmoid, relu, elu
    
def calc_activation_func(x, act_name):
    if act_name == 'sigmoid' :
        return sigmoid(x)
    elif act_name == 'relu' :
        return relu(x)
    elif act_name == 'elu' :
        return elu(x)

if __name__ == '__main__':
    print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))