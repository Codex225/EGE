def f(x):
    P = 10 <= x <= 20
    Q = 35 <= x <= 45
    A = a1 <= x <= a2
    return ((not P) <= Q) and (not A)

dots = []
for x in (10, 20, 35, 45):
    dots.append(x)
    dots.append(x + 0.1)
    dots.append(x - 0.1)
res = []
for a2 in dots:
    for a1 in dots:
        if a2 > a1 and all( (not f(x)) for x in dots):
            res.append(round(a2 - a1))
print(min(res))