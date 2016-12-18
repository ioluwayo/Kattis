#solved
def removedups(name):
    x=[]
    for i in range(len(name)-1):
        if name[i] != name[i+1]:
            x.append(name[i])
    x.append(name[-1])
    return "".join(x)
infile = open("test/apaxiaaans-003.in")
name  = infile.readline().strip()
namearr = map(str,(i for i in name))
print removedups(namearr)
