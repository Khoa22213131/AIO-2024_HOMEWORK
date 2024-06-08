from TL.ex2 import sigmoid, relu, elu
    
def calc_activation_func(x, act_name):
    if act_name == 'sigmoid' :
        return sigmoid(x)
    elif act_name == 'relu' :
        return relu(x)
    elif act_name == 'elu' :
        return elu(x)

print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))