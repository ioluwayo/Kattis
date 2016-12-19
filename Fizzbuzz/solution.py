infile = open("tests/fizzbuzz-03.in")
x,y,n = map(int,infile.readline().strip().split(" "))
for i in xrange(1,n+1):
    if i%x == 0 and i%y == 0:
        print "FizzBuzz"
    elif i%x == 0:
        print "Fizz"
    elif i%y == 0:
        print "Buzz"
    else:
        print i
