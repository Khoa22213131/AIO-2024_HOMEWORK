import math
import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        sum_exp = torch.sum(torch.exp(x), dim=0)
        return torch.exp(x) / sum_exp


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        max = torch.max(x)
        sum_exp = torch.sum(torch.exp(x - max), dim=0)
        return torch.exp(x - max) / sum_exp


if __name__ == '__main__':
    # Examples 1
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)

    data = torch.Tensor([1, 2, 3])
    softmax_stable = softmax_stable()
    output = softmax_stable(data)
    print(output)
