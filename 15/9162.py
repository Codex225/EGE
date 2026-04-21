def sqr(a, b, c):
    return a * b > c

def f(x, y, a):
    return (not sqr(x, y, a + 13)) <= (sqr(28, y, 520) or sqr(x, 25, 800))

for a in range(-100, 1000):
    if all(f(a,x,y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)