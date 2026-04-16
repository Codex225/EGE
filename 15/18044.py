def f(x):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = a1 <= x <= a2
    return (not (M or N)) == (not A)

dots = []
for x in (32, 68 , 54, 76):
    dots.append(x)
    dots.append(x + 0.1)
    dots.append(x - 0.1)

res = []
for a1 in dots:
    for a2 in dots:
        if a2 > a1 and all(f(x) for x in dots):
            res.append(round(a2 - a1))
print(min(res))