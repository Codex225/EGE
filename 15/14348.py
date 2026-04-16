def f(x, a):
    return  (x & 47 == 0) or ((x & 13 == 0) <=  (not (x & a == 0)))

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
        break