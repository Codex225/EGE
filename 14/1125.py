def f4(n):
    res = []
    while n:
        res.append(n % 4)
        n //= 4
    return res[::-1]

for x in range(1, 100000):
    n = 64**11 - 4**10 + 96 - x
    if sum(f4(n)) == 71:
        print(x)
        