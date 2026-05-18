from itertools import *
q = 0
for w in set(permutations("СОТОЧКА")):
    s = "".join(w)
    for x in "ОА": s = s.replace(x, "*")
    print(s)
    if "**" in s:
        q += 1
print(q)