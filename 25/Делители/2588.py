def dels(n):
    res = set()
    for x in range(1, int(n**0.5) +1):
        if n % x == 0:
            res.add(x)
            res.add(n // x)
    return sorted(list(res))

for n in range(190_201, 190_260 + 1):
    r = dels(n)
    rr = [x for x in r if x% 2 ==0]
    if len(rr) == 4:
        print(rr[3], rr[2])
