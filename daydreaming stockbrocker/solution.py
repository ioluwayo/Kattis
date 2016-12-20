#solved
infile = open("tests/1.in")
numberOfDays = int(infile.readline().strip())
availableMoney = 100
sharesOwned = 0
maxShares = 100000
if numberOfDays == 1:
    print availableMoney
    exit()
todaysPrice = int(infile.readline().strip())
for i in xrange(numberOfDays-1):
    tomorrowsPrice = int(infile.readline().strip())
    if tomorrowsPrice > todaysPrice:
        if sharesOwned<maxShares and availableMoney:
            #buy some more
            sharesOwned+=availableMoney/todaysPrice
            availableMoney-=(availableMoney/todaysPrice)*todaysPrice
            if sharesOwned>maxShares:
                excess = sharesOwned-maxShares
                availableMoney+=excess*todaysPrice
                sharesOwned-=excess
    elif tomorrowsPrice < todaysPrice:
        # sell everything
        availableMoney+=todaysPrice*sharesOwned
        sharesOwned = 0
    todaysPrice=tomorrowsPrice
if sharesOwned:
    availableMoney+=todaysPrice*sharesOwned
    sharesOwned = 0
print availableMoney