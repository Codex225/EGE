def tri(a, b, c):
    return a + b > c and b + c > a and c + a > b

def mm(a, b):
    if a > b:
        return a
    return b

def f(a, x):
    return tri(a, 5, x) <= ((mm( x, 11) <= 19) == (not (tri(23, 13, x))))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)