def f(x, y):
    return (x >= 11) or (3 * x < y) or (x * y < a)
res = []

for a in range(500):
    if all([f(x, y) for y in range(500) for x in range(500)]):
        res.append(a)
print(min(res))