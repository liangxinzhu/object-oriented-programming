import math

def isprime(n):
    a = math.floor(math.sqrt(n))
    for i in range(2,a+1):
        if n%i == 0:
            return('False')
        else:
            continue
    return('True')
        
