def f(x):
    P = 3 <= x <= 15
    Q = 14 <= x <= 25
    A = a1 <= x <= a2
    return (P == Q) <= (not A)

dots = []
for i in (3, 15, 14, 25):
    dots.append(i)
    dots.append(i + 0.1)
    dots.append(i - 0.1)
res = []
for a1 in dots:
    for a2 in dots:
        if a2 > a1 and all(f(x) for x in dots):
            res.append(round(a2 - a1 ))


print(max(res))