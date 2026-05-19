from itertools import *
q = 0
for w in product(sorted("ЯНВАРЬ"), repeat=5):
    s = "".join(w)
    q += 1
    #print(s, q)
    if s[0] != "Я" and s.count("Ь") <= 1 and "ЯЯ" not in s:
        print(q)