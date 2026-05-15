for n in range(10000, 100000):
    d = [int(x) for x in str(n)]
    qs = (min(d) + max(d))**2
    prchd = 1
    for x in d:
        if x % 2 == 0:
            prchd *= x
    r = []
    r.append(prchd)
    r.append(qs)
    r.sort(reverse=True)
    res = int("".join([str(x) for x in r]))
    if res == 12116:
        print(n)