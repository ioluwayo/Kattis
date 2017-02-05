#solved
infile = open("tests/a.in")
tests = int(infile.readline())
for i in xrange(tests):
    infile.readline()
    totalCandies = 0
    numberOfKids = int(infile.readline())
    for i in xrange(numberOfKids):
        totalCandies += long(infile.readline())
    if totalCandies % numberOfKids:
        print "No"
    else:
        print "Yes"