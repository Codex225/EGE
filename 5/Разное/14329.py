def f4(n):
    s = ""
    while n:
        s += str(n % 4)
        n //= 4
    return s[::-1]
minr = 100000000000
for n in range(1, 100000):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4[:2] + n4
    else:
        n4 = n4 + f4((n % 4) * 4)
    res = int(n4, 4)
    if res > 291:
        minr = min(minr, res)
print(minr)