from itertools import *
q = 0
for w in product(sorted(set("СУБЛИМАЦИЯ")), repeat=5):
    s = ''.join(w)
    q += 1
    if q % 2 == 1 and s[-1] != "Я":
        for x in "УИАЯ": s = s.replace(x, "*")
        if s.count("*") == 2:
            print(s, q)