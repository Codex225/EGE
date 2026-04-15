def f(x):
    return (x & 57 == 0) or ( (x & 23 == 0) <= (not(x & A == 0)))

for A in range(1, 100000):
    if all(f(x) for x in range(0, 100000)):
        print(A)
        break