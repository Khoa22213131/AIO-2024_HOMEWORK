import math

def is_number (n) :
    try :
        float (n) 
    except ValueError :
      return False
    return True

print ( is_number (1) )
print ( is_number ('n') )