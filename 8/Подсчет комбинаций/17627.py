from itertools import *
q = 0
for w in product("0123456789abcde", repeat=5):
    s = "".join(w)
    if s.count("8") == 1 and s[0] != "0":
        for x in  "abcde": s = s.replace(x, "*")
        if s.count("*") >= 2:
            q += 1
print(q)