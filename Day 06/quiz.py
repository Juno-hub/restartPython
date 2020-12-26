# Q) You are taxi driver belong to Cocoa.
# Find total number of passenger when you have chance that match 50 passenger.

# rule 1: Total elapsed time is random between 5 min and 50 min
# rule 2: You must find passenger of the elapsed time between 5 min and 15 min

# (Output Example)
# [O] No.1 passenger (the elapsed time: 15 min)
# [ ] No.2 passenger (the elapsed time: 50 min)
# [O] No.3 passenger (the elapsed time: 5 min)
# ...
# [ ] No. 50 passenger (the elapsed time: 16 min)

# Total number of passenger: 2

# My answer
from random import *

i = 1
count = 0

while i < 51:
    time = randint(5, 50)
    if 5 <= time <= 15:
        print("[O] No.{0} passenger (the elapsed time: {1} min)".format(i, time))
        count += 1
    else:
        print("[ ] No.{0} passenger (the elapsed time: {1} min)".format(i, time))
    i += 1

print("Total number of passenger: {0}".format(count))

# 나도코딩 answer
from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] No.{0} passenger (the elapsed time: {1} min)".format(i, time))
        cnt += 1
    else:
        print("[ ] No.{0} passenger (the elapsed time: {1} min)".format(i, time))

print("Total number of passenger: {0}".format(cnt))

# Debriefing
# Perfect!