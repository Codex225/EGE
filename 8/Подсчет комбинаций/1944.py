from itertools import *
q = 0
alf = "одеколон"
for w in set(permutations(alf)):
    s = "".join(w)
    if "оо" not in s and "ооо" not in s:
        q += 1
print(q)