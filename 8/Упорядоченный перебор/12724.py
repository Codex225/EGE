from itertools import *
q = -1
for w in product(sorted(set("КАЛЕЙДОСКОП"),reverse=True), repeat=6):
    s = "".join(w)
    q += 1
    if s[0] == "К" and s.count("Й") == 2 and "С" not in s and "Е" not in s and q % 2 == 0:
        print(s, q)
        break
