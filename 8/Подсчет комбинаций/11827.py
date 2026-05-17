from itertools import *

q = 0
for w in product("01234567", repeat=7):
    s = "".join(w)
    if s[0] != "0":
        for x in "0246": s = s.replace(x, "*")
        for x in "135": s =s.replace(x, "-")
        if s.count("*") == 2 and "-7" not in s and "7-" not in s and "77" not in s:
            q +=1
print(q)