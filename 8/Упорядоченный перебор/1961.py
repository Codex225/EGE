from itertools import *
q = 0
for w in product(sorted("ЛЕМУР"), repeat=4):
    s = "".join(w)
    q += 1
    if s[0] == "Л":
        print(s, q)
        break