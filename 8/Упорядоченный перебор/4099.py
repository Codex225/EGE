from itertools import *
q = 0
for w in product(sorted("БУЛКА"), repeat=4):
    s = "".join(w)
    q += 1
    if len(set(s)) == 4:
        print(s, q)