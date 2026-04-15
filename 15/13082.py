def f(x, y):
    return ((3 * x + y) > 48) or (x > y) or ((4 * x + y) < a )

for a in range(1, 1000):
    if not all([f(x, y) for x in range(0, 1000) for y in range(0, 100)]):
        print(a)