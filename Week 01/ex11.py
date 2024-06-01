import math

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += x**(2*i+1) / math.factorial(2*i+1)
    return result

print ( round ( approx_sinh ( x =3.14 , n =10) , 2) )