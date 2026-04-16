def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = a1 <= x <= a2
    return (A and (not Q)) <= (P or Q)

dots=[]
for x in (25, 73, 75, 118):
    dots.append(x)
    dots.append(x + 0.1)
    dots.append(x - 0.1)

from math import *
res = []
for a1 in dots:
    for a2 in dots:
        if a2 > a1 and all(f(x) for x in dots):
            res.append(round(a2 - a1 ))
print(max(res))
