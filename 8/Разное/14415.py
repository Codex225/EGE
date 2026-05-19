from itertools import *
q = 0
alf = "0123456789ab"
for w in product(alf, repeat=5):
    s = "".join(w)
    if s.count("a") == 2 and s[0] != "0":
        for x in "02468a": s= s.replace(x, "*")
        if "*7" not in s and "7*" not in s:
            q += 1
print(q)