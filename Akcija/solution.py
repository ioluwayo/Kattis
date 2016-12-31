#solved
def calculatePrice(prices):
    prices.sort(reverse=True)
    price = 0
    for i in xrange(0,len(prices),3):
        price+=prices[i];
        if i+1 < len(prices):
            price+=prices[i+1]
    print price
infile = open("tests/akcija.2.in")
numberOfItems = int(infile.readline())
prices = []
while numberOfItems:
    prices.append(int(infile.readline().strip()))
    numberOfItems -= 1
calculatePrice(prices)
