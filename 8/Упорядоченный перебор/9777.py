from itertools import *
q = 0
for w in product(sorted("КОМПЬЮТЕР"), repeat=5):
    s = "".join(w)
    q +=1
    if s[0] != "Ь" and s.count("К") == 2 and q % 2 == 1:
        print(s, q)