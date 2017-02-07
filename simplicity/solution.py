# solved
import collections
infile = file("tests/Complexity-0006.in")
word =  infile.readline().strip()

def getSimplicity(word):
    simplicity = len(set(word))
    if simplicity  <= 2:
        return 0
    else:
        return simplicity
def deleteStuff(word):
    dictionary = dict(collections.Counter(word))
    items = dictionary.items()
    items.sort(key=lambda item: item[1])
    orderedItems = [i[0] for i in items]
    num = dictionary[orderedItems[0]]
    word = word.replace(orderedItems[0],"")
    return num, word
count = 0

while getSimplicity(word) > 2:
    num,word = deleteStuff(word)
    count += num
print count