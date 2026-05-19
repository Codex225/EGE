from itertools import *
q = 0
c = 0
for w in product(sorted("ПРЕСТОЛ"), repeat=5):
    s = "".join(w)
    q += 1
    if q % 2 == 1 and s[-1] in "ЕО":
        for x in "ПРСТЛ": s = s.replace(x, "*")
        if s.count("*") <= 3:
            c += 1
print(c)