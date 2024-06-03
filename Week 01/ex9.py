import math

def approx_cos(x, n) :
    result = 0
    for i in range (n) :
        result += ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    return result

print(round(approx_cos(x=3.14, n=10), 2))