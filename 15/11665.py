def mo(x, y):
    return x % y

def f(x, a):
    return (a + x > 700 - a) and (mo(a, 100) + mo(100, x) > 50)

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)