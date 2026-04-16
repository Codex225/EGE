def f(x):
    P = 5 <= x <= 280
    Q = 295 <= x <= 400
    R = 375 <= x <= 450
    A = a1 <= x <= a2
    return (Q  <=  P) or ((not A) <= R)

dots = []
for x in (5, 280, 295, 400, 375, 450):
    dots.append(x)
    dots.append(x + 0.1)
    dots.append(x - 0.1)


res = []
for a1 in dots:
    for a2 in dots:
        if a2 > a1 and all(f(x) for x in dots):
            res.append(round(a2 - a1))
print(min(res))

