from itertools import *
q = 0
for w in permutations("дейкстра", r=6):
    s = "".join(w)
    for sog in "дкстр": s = s.replace(sog, "1")
    if "й1" in s:
        q += 1
print(q)
