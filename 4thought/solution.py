#unsolved
from itertools import combinations_with_replacement
def do4thought(n):
    operations = ["+","-","*","/"]
    for i in combinations_with_replacement(operations,3):
        fours = [int(4),int(4),int(4),int(4)]
        fours.insert(1,i[0])
        fours.insert(3,i[1])
        fours.insert(5,i[2])
        fours =  " ".join(str(x) for x in fours)
        if eval(fours) == n:
                return fours + " =" + " "+str(n)
    for i in combinations_with_replacement(reversed(operations),3):
        fours = [int(4), int(4), int(4), int(4)]
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
#print map (lambda x:x, (i for i in permutations([6,8,9])))
    print do4thought(n)