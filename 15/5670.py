def dell(n, m):
    return n % m == 0

def summbol(s, d):
    return s + d > 0

def f(x):
    return (x + a >= 160) or (dell(x, 7) <= (not summbol(x, - 17)))

for a in range(1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break