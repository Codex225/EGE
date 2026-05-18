from itertools import *
q = 0
for w in product("0123456789ab", repeat=7):
    s = "".join(w)
    if s[0] != "0":
        for x in "0369": s = s.replace(x, "0")
        for x in "124578ab": s = s.replace(x, "1")
        print(s)
        if s == "1010101" or s== "0101010":
            q += 1
print(q)