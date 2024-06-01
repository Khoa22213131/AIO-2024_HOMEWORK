import math

def approx_sin (x , n ) :
    result = 0
    for i in range (n) :
        result += ((-1)**i) * (x**(2*i+1)) / math.factorial(2*i+1)
    return result
print ( round ( approx_sin ( x =3.14 , n =10) , 4) )