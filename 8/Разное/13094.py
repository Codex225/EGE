from itertools import *
q = 0
for w in product("012345678", repeat=9):
    s = "".join(w)
    if "0" not in s:
        spr = s
        for x in "02468": spr = spr.replace(x, "*")
        for x in "1357": spr = spr.replace(x, "+")

        if all([s.count(x) <= 3 for x in s]) and "++" not in spr and "**" not in spr:
            q += 1

print(q)