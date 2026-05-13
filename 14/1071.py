def f5(n):
    res = []
    while n:
        res.append(n % 5)
        n //= 5
    return res[::-1]

for x in range(1, 1000):
    n = 125**200 - 5**x + 74
    n5 = f5(n)
    if n5.count(4) == 100:
        print(x)

