def f(x):
    P = 25 <= x <= 50
    Q = 32 <= x <= 47
    A = a1 <= x <= a2
    return ((not A) <= P) <= (A <= Q)

res = []
d = [y for x in[25, 50, 32, 47] for y in [x + 0.1, x - 0.1, x]]
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all([f(x) for x in d]):
            res.append(a2 - a1)
print(max(res))
