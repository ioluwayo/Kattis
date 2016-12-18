#solved!
def primaryScore(arr):
    n = 0
    for i in xrange(len(arr)):
        if arr[i]["pass"]  == "right":
            n=n+1
    return n
def secondaryScore(arr):
    #creat unique set of the problems.
    score = sum(x["time"] for x in arr if x["pass"]  == "right")
    rights = map(lambda x:x, ([x["prob"], x["time"]] for x in arr if x["pass"] == "right"))
    wrongs = map(lambda x:x, ([x["prob"], x["time"]] for x in arr if x["pass"] == "wrong"))
    rr=[]
    for wrong in wrongs:
        for right in rights:
            if wrong[0] == right[0]:
                score+=20
    return(score)

infile = open("test/1.in")
entry = infile.readline().strip().split(" ")

arr = []
while int(entry[0]) is not -1:
    arr.append({"time":int(entry[0]),"prob":str(entry[1]),"pass":str(entry[2])})
    entry = infile.readline().strip().split(" ")
print primaryScore(arr),secondaryScore(arr)