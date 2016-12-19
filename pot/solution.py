#solved
from math import pow
infile = open("tests/pot.3.in")
ps = int(infile.readline().strip())
value = 0
for i in xrange(ps):
    s = map(str,infile.readline().strip())
    arr=list(s)
    power = int(arr.pop())
    number = int("".join(arr))
    value += int(pow(number,power))
print value