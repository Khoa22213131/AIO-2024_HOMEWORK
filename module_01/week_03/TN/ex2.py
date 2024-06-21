import torch
import torch.nn as nn

class MySoftmax (nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        sum_exp = torch.sum(torch.exp(x), dim = 0)
        return torch.exp(x) / sum_exp

        
data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output = my_softmax(data)

print(output)