from itertools import *
q = 0
for w in product("012345678", repeat=5):
    s = "".join(w)
    #print(s)
    if s.count("5") == 1 and s[0] != "0" and not any([x * 2 in s for x in s]):
        q +=1
print(q)