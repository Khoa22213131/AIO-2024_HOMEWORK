#Viết function lựa chọn regression loss function để tính loss:

import math
import random


def mse(n_samples):
    if not n_samples.isnumeric():
        print('number of samples must be a integer')
        return
    
    n_samples = int(n_samples)
    
    y = []
    y_hat = []
    
    for _ in range(n_samples):
        y.append(random.uniform(0, 10))
        y_hat.append(random.uniform(0, 10))
    
    return sum([(y[i] - y_hat[i])**2 for i in range(n_samples)]) / n_samples

def mae(n_samples):
    if not n_samples.isnumeric():
        print('number of samples must be a integer')
        return
    
    n_samples = int(n_samples)
    
    y = []
    y_hat = []
    
    for _ in range(n_samples):
        y.append(random.uniform(0, 10))
        y_hat.append(random.uniform(0, 10))
    
    return sum([abs(y[i] - y_hat[i]) for i in range(n_samples)]) / n_samples

def rmse(n_samples):
    
    return math.sqrt(mse(n_samples))

def regression_loss_function(name='mse', n_samples=100):
    if name == 'mse':
        return mse(n_samples)
    elif name == 'mae':
        return mae(n_samples)
    elif name == 'rmse':
        return rmse(n_samples)
    else:
        print('Invalid loss function')
        return