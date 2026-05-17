from itertools import *
q = 0
q2 = 0
res1 = []
res2 = []
for w in product(sorted("НОРМАЛЬЕ"), repeat=6):
    s = "".join(w)
    q += 1
    print(s)
    if s == "НЕНОРМ":
        q1 = q
    if s[:4] == "НОРМ":
        q2 = q
        break
print(q1, q2, q2-q1 - 1)