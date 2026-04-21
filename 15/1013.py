def f(x):
    P = 23 <= x < 45
    Q = 34 <= x <= 56
    A = a1 <= x <= a2
    return (not A) or (not P) and Q

dots = []
for i in (23, 45, 34, 56):
    dots.append(i)
    dots.append(i + 0.1)
    dots.append(i - 0.1)
res = []
for a1 in dots:
    for a2 in dots:
        if a2 > a1 and all(f(x) for x in range(-1000, 10000)):
            res.append(round(a2 - a1))
print(max(res))