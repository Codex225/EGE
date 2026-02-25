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

q = 0
for n in range(987_654_321, 985_650_321, -1):
    m = fn(n)
    if len(m) == 13 and "1" in str(sum(m)):
        q += 1
        print(n, max(m))
        if q == 5:
            break