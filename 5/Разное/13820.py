def f3(n):
    s = ""
    while n:
        s += str(n % 3)
        n //= 3
    return s[::-1]
rmin = 100000000000
for n in range(1, 10000):
    n3 = f3(n)
    if n % 7 == 0:
        n3 = n3 + n3[-2:]
    else:
        n3 = n3 + f3((n % 7) * 3)
    r = int(n3, 3)
    if r > 369:
        rmin = min(rmin, r)
print(rmin)