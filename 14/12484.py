def f5(n):
    res = []
    while n:
        res.append(n % 5)
        n //= 5
    return res[::-1]

for x in range(1, 100):
    for y in range(1, 100):
        d = 5**50 + 5**30 - 5**x - y - 5**y - x
        if d < 0: continue
        d5 = f5(d)
        if d5.count(0) == 10:
            print(x * y)