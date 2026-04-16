def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = a1 <= x <= a2
    return (Q <= (not R)) and A and (not P)

dots = []
for i in (10, 25, 15, 30, 25, 40):
    dots.append(i)
    dots.append(i + 0.1)
    dots.append(i - 0.1)

res = []
for a2 in dots:
    for a1 in dots:
        if a2 > a1 and all((not f(x)) for x in dots):
            res.append(round(a2 - a1))
print(max(res))