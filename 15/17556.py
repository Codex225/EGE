def f(x):

    B = 70 < x < 90
    return (x % a == 0) or ( B <= (not(x % 22 == 0)))
for a in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(a)