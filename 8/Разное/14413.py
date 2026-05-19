from itertools import *
q = 0
for w in set(permutations("СОРТИРОВКА")):

    s = "".join(w)
    for x in "СРТРВК": s = s.replace(x, "*")
    for x in "ОИОА": s = s.replace(x, "+")
    print(s)
    if "***" not in s and "+++" not in s:
        q = q + 1
print(q)