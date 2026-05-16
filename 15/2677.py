def f(x):
    D = 12 <= x <= 20
    C = 31 <= x <= 45
    A = a1 <= x <= a2
    return (not C) and (not D) or ((D or C) <= A)

dots = []
for i in (12, 20, 31, 45):
    dots.append(i)
    dots.append(i + 0.1)
    dots.append(i - 0.1)
res = []
for a1 in dots:
    for a2 in dots:
        if a2 > a1 and all(f(x) for x in dots):
            res.append(round(a2 - a1 ))


print(max(res))