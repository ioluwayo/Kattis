# solved
# lol this is way more efficient.
# the army with the strongest soldier wins regardless of the sizes of the armies
tests = int(raw_input())
for i in xrange(tests):
    raw_input()
    raw_input()
    earthArmy = map(int, raw_input().split(" "))
    alienArmy = map(int, raw_input().split(" "))
    if max(earthArmy)<max(alienArmy):
        print "MechaGodzilla"
    else:
        print "Godzilla"