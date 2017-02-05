# Created by ioluwayo on 2017-02-05.
# solved
numbers = map(int,raw_input().strip().split(" "))
request = raw_input().strip()
letters = "ABC"
numb =  sorted(numbers)
lookUp = dict(zip(letters,numb))
print lookUp[request[0]],lookUp[request[1]],lookUp[request[2]]