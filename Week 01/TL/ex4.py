#Viết 4 functions để ước lượng các hàm số sau.
import math

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def sin(x, n):
    if n <= 0:
        print('n must be a positive integer')
        return
    
    result = 0
    for i in range (n):
        result += ((-1)**i) * (x**(2*i+1)) / factorial(2*i+1)
    return result

def cos(x, n):
    if n <= 0:
        print('n must be a positive integer')
        return
        
    result = 0
    for i in range (n):
        result += ((-1)**i) * (x**(2*i)) / factorial(2*i)
    return result

def sinh(x, n):
    if n <= 0:
        print('n must be a positive integer')
        return
    
    result = 0
    for i in range (n):
        result += (x**(2*i+1)) / factorial(2*i+1)
    return result

def cosh(x, n):
    if n <= 0:
        print('n must be a positive integer')
        return
    
    result = 0
    for i in range (n):
        result += (x**(2*i)) / factorial(2*i)
    return result