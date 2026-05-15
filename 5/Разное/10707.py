def f6(n):
    s = ""
    while n:
        s += str(n % 6)
        n //= 6
    return s[::-1]
mr = 10000000
for n in range(1,1000):
    n6 = f6(n)
    if n % 3 == 0:
        n6 = n6 + n6[:2]
    else:
        n6 = n6 + f6((n % 3) * 10)
    r = int(n6, 6)
    if r > 680:
        mr = min(mr, r)
print(mr)