# Created by ioluwayo on 2017-02-06.
# Solved
def rule1(seq):
    rule = "U"
    count = 0
    state = seq[0]
    seq = seq[1:]
    for preference in seq:
        if preference != state:
            count += 1 #change the seat
            state =preference
            if state != rule:
                count += 1
                state = rule
        else:
            if state != rule:
                count += 1
                state = rule
    return count
def rule2(seq):
    rule = "D"
    count = 0
    state = seq[0]
    seq = seq[1:]
    for preference in seq:
        if preference != state:
            count +=1
            state = preference
            if state == rule:
                count += 0
            else:
                count +=1
                state = rule
        else:
            if state == rule:
                count +=0
            else:
                count +=1
                state =rule
    return count
def rule3(seq):
    count = 0
    state = seq[0]
    seq = seq[1:]
    for preference in seq:
        if preference != state:
            count+=1
            state = preference
    return count

infile = open("toilet-1.in")
seq = map(str,infile.readline().strip())
print seq

print rule1(seq)
print rule2(seq)
print rule3(seq)