#solved
infile = open("tests/4.in")
no_problems,index_of_first =  map(int,infile.readline().strip().split(" "))
legnths_to_solve = map(int,infile.readline().strip().split(" "))
legnth_to_solve_first = legnths_to_solve.pop(index_of_first)
time_penalty = 0
time_left  = 300
count = 0
legnths_to_solve.sort()
legnths_to_solve.insert(0,legnth_to_solve_first)
while len(legnths_to_solve):
    lent = legnths_to_solve.pop(0)
    time_left-=lent
    if time_left>=0:
        count+=1
        time_penalty+=300-time_left
print count, time_penalty