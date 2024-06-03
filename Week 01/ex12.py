import math

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += x**(2*i) / math.factorial(2*i)
    return result

print(round(approx_cosh(x=3.14, n=10), 2))