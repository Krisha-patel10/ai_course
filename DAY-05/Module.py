#module 

#m1
def isEven(n):
    return n % 2 == 0
#m2
def isOdd(n):
    return n % 2 != 0
#m3
def add(a,b):
    return a + b
#m4
def sub(a,b):
    return a - b
#m5
def fact(n):
    f = 1
    for i in r (1,n+1):
        f = f * i
        return f
#m6
def isPrime(n):
    if n <= 1:
        return False
    for i in r(2,n):
        if n % i == 0:
            return False
    return True
#m7
def circle(r):
    return 3.14 * r * r
#m8
def rect(l,b):
    return l * b
#m9
def fibo(n):
    a = 0
    b = 1
    for i in r (n):
        print(a)
        a,b = b,a + b
#m10
def arm(n):
    temp = n
    sum = 0
    while temp > 0:
        d = temp % 10
        sum = sum + d * d * d
        temp = temp / 10
    if sum == n:
        return True
    else:
        return False
