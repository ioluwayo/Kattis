#solved
from math import sqrt
def isprime(n):
    if n<2:
        return False
    else:
        for i in xrange(2,int(sqrt(n)+1)):
            if n%i == 0:
                return False
        return True

def countdivides(n):
    #prime numbers are the easiest cases, so check if primes first
    # dramatically improves performance when n is a large prime number
    if isprime(n):
        return 1
    d = 2;
    count = 0
    while n>1:
        if n%d==0:
            n = n/d
            d=2
            count+=1
        else:
            d+=1
    return count
infile = open("tests/listgame.01.in")
number = int(infile.readline())
print countdivides(number)