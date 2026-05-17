from itertools import *
q = 0

for w in product(sorted("мария"), repeat=4):
    s = "".join(w)
    q += 1
    print(s, q)
    if q == 211:
        print(s)
        break