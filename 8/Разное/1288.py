from itertools import *
q = 0
for w in product("ВИШНЯ", repeat=6):
    s = "".join(w)
    if s.count("В") <= 1 and s[0] not in "Ш" and s[-1] not in "ИЯ":
        q += 1
print(q)