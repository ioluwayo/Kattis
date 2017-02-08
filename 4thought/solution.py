#solved
from itertools import product
def do4thought(n):
    operations = ["+","-","/","*"]
    for i in product(operations,repeat = 3):
        fours = [4, 4, 4, 4]
        fours.insert(1,i[0])
        fours.insert(3,i[1])
        fours.insert(5,i[2])
        fours =  " ".join(str(x) for x in fours)
        if eval(fours) == n:
                return fours + " =" + " "+str(n)
    for i in product(reversed(operations),repeat = 3):
        fours = [4, 4, 4, 4]
        fours.insert(1, i[0])
        fours.insert(3, i[1])
        fours.insert(5, i[2])
        fours = " ".join(str(x) for x in fours)
        if eval(fours) == n:
            return fours + " =" + " " + str(n)
    return "no solution"
infile = open("tests/4thought.in")
tests = int(infile.readline().strip())
for i in xrange(tests):
    n = int(infile.readline().strip())
    print do4thought(n)