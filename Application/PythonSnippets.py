'''
Print Even number
'''
class customException(Exception):
    pass

def GenEvenNums(num):
    evennum = []
    for i in range(1,num+1):
        if i%2==0:
            evennum.append(i)
    return evennum

def check_prime(num):
    Primeflag = True
    if type(num) != int:
        raise customException("input should be an integer")
    if num<=1:
        return False
    else:
        for i in range(2,num//2):
            if num%i==0:
                Primeflag = False
                break
    return Primeflag

def add(a,b):
    return a+b

def concat(a,b):
    if type(a)==str or type(b)== str:
        return(a+b)        
    else:
        raise("not a correct input for concatination")

