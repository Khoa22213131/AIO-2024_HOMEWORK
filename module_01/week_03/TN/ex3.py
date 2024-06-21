import torch
import torch.nn as nn


class MySoftmax (nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        sum_exp = torch.sum(torch.exp(data), dim = 0)
        return torch.exp(data) / sum_exp

data = torch.Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)

print(output)
