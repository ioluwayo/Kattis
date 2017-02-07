# Created by ioluwayo on 2017-02-06.
# solved
infile = open("1.in")
cases = int(infile.readline())
for i in xrange(cases):
    sentence = infile.readline().replace("\n","")
    dictionary = {"a":'2',"b":'22',"c":'222',"d":'3',"e":'33',"f":'333',"g":'4',
                  "h":'44',"i":'444',"j":'5',"k":'55',"l":'555',
                  "m":'6',"n":'66',"o":'666',"p":'7',"q":'77',"r":'777',
                  "s":'7777',"t":'8',"u":'88',"v":'888',"w":'9',"x":'99',
                  "y":'999', "z":'9999', ' ':'0'}
    answer = ""
    previous = -1
    for word in sentence:
        for letter in word:
            if int(dictionary[letter][0]) == previous:
                answer = answer+" "
            answer = answer + dictionary[letter]
            previous = int(dictionary[letter][0])
    print "Case #"+ str(i+1)+":",answer
