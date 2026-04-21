def f(x, y):
    return ((x > 8) <= (x *x + 3 * x >= a)) and ((y * y + 5 * y > a) <= (y >= 4))
q = 0
for a in range(-1000, 1000):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        q += 1
print(q)
