from itertools import *
q = 0
for w in product("01234567", repeat=5):
    if w[0] not in "01357" and w[-1] not in "26" and w.count("7") <= 2:
        q +=1
print(q)
