a = int(input('a : '))
b = int(input('b : '))
def two_plus():
    return a+b

two_plus()
#-----------------위와 아래는 같음--------------- 
def two_plus(c, d):
    return c+d
a = int(input('a : '))
b = int(input('b : '))

two_plus(a,b)
