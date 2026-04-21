def f(x, y, a):
    return (x < 7) or ( y >= 3 * x + a - 20) or (x >= 34) or (y < 121)

for a in range(500):
    if all(f(x, y, a) for x in range(500) for y in range(500)):
        print(a)