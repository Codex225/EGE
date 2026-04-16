def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

dots = []
for i in (15, 40, 21, 63):
    dots.append(i)
    dots.append(i - 0.1)
    dots.append(i + 0.1)

res = []
for a1 in dots:
    for a2 in dots:
        if a2 > a1 and all(f(x) for x in dots):
            res.append(round(a2 - a1))
print(min(res))