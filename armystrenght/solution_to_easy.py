# solved
# used the timer to compare the efficiency of this solution and that of the "hard" version of the challenge
import time
starttime = time.time()
infile = open("test/sample.in")
tests = int(infile.readline().strip())
for i in xrange(tests):
    infile.readline()
    infile.readline()
    earthArmy = map(int, infile.readline().strip().split(" "))
    aleinArmy = map(int,infile.readline().strip().split(" "))
    earthArmy.sort()
    aleinArmy.sort()
    while len(earthArmy) and len(aleinArmy):
        weakestAlien = aleinArmy[0]
        weakestHuman = earthArmy[0]
        if weakestAlien == weakestHuman:
            aleinArmy.pop(0)
        elif weakestHuman<weakestAlien:
            earthArmy.pop(0)
        elif weakestAlien<weakestHuman:
            aleinArmy.pop(0)
        else:
            break
    if len(earthArmy) == 0:
        print "MechaGodzilla"
    elif len(aleinArmy) == 0:
        print "Godzilla"
print ("--- %s seconds ---" % (time.time() - starttime))