def fn(n):
    m = []
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
             m += [d]
             n = n // d
        else:
            d += 1

    if n > 1:
        m += [n]
    return m

for n in range(15_381_265, 15_385_000):
    m = fn(n)
    if len(m) == 3 and str(m[0]).count("1") == str(m[1]).count("1") == str(m[2]).count("1") == 1:
        print(n, max(m))
