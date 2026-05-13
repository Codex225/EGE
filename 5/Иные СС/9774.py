def f3(n):
    res = ""
    while n:
        res += str(n % 3)
        n = n // 3
    return res[::-1]

mr = 10**100000
for n in range(1, 100000):
    n3 = f3(n)
    if n % 3 == 0:
        n3 = n3 + n3[-2] + n3[-1]
    else:
        n3 = n3 + f3(5* (n % 3))

    r = int(n3, 3)
    if r > 133:
        mr = min(mr, r)
print(mr)