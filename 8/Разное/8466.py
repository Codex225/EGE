from itertools import *
q = 0
for w in product("0123456", repeat=6):
    if w[0] != "0" and w[-1] not in "0123":
        s = "".join(w)
        for x in "0246": s = s.replace(x, "2")
        for x in "135": s = s.replace(x, "1")
        if s.count("1") == s.count("2"):
            q += 1
print(q)