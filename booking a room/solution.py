#solved
infile = file("tests/2.in")
numberOfRooms,numberOfRoomsBooked = map(int,infile.readline().split())
if numberOfRoomsBooked == numberOfRooms:
    print "too late"
else:
    bookedRooms = []
    for i in xrange(numberOfRoomsBooked):
        bookedRooms.append(int(infile.readline()))
    bookedRoomsDictionary = {x:x for x in bookedRooms}
    d = bookedRoomsDictionary.get(4)
    for i in xrange(1,numberOfRooms+1):
        if not bookedRoomsDictionary.get(i):
            print i
            break