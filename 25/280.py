def dels(n):
    r = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)

for n in range(333_555, 777_999 + 1):
    res = [x for x in dels(n) if len(str(x)) == 2 ]
    if len(res) == 35:
        print(res[0], res[-1])