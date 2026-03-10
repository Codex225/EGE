def mn(n):
    d = 2
    m = []
    while d ** 2 <= n:
        if n % d == 0:
            
            m.append(d)
            n = n // d
        else:
            d += 1
    return m + [n]

for n in range(5_000_000, 5_000_100):
    m = mn(n)
    if len(m) == 3 and all("2" in str(d) or "3" in str(d) for d in m):
        print(n)