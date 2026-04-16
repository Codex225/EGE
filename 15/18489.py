def cc(x, y):
    return x % 10 == y % 10

def f(x, a):
    return ((not cc(x, 5)) and cc(x, 4)) <= (x > a - 11)

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)