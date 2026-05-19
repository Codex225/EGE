from itertools import *
q = 0
alf = "0123456789ab"
for w in product(alf, repeat=6):
    s = "".join(w)
    if s[0] != "0" and s.count("b") == 1:
        for x in "02468a": s=s.replace(x, "*")
        for x in "13579b": s=s.replace(x, "+")
        if s.count("*") == s.count("+"):
            q +=1
print(q)