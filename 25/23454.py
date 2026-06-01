def fact(n):
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)
    return res

for n in range(1_561_330 + 1, 1_570_000):
    res = fact(n)
    if len(res) == 3:
        if str(sum(res)) == str(sum(res))[::-1]:
            print(n, sum(res))