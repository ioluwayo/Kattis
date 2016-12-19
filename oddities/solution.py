#solved
infile = open("tests/sample.in")
tests = int(infile.readline().strip())
while tests:
    number = int(infile.readline().strip())
    if(abs(number)%2==0):
        print number,"is even"
    else:
        print number,"is odd"
    tests=tests-1