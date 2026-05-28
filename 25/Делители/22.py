def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:

            res.add(i)
            res.add(n // i)

    return list(res)

dels =[]
for n in range(174457, 174505 + 1):
    r = sorted(f(n))

    if len(r) == 2:
        print(*r)



