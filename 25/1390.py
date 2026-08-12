def dels(n):
    r = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)

for n in range(350_000, 352_000):
    res = dels(n)
    if len(res) <= 1:
        m = 0
    else:
        m = res[-1] - res[0]
    if m % 23 == 9:
        print(n, m)