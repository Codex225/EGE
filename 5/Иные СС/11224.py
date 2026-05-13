def f3(n):
    res = []
    while n:
        res.append(n % 3)
        n = n // 3
    return res[::-1]
rm = 100000
for n in range(1, 100000):
    n3 = f3(n)
    if sum(n3) % 4 == 0:
        n3 = "1" + "".join(map(str, n3))[:-2]
    else:
        n3 = "".join(map(str, n3)) +  "".join(map(str, f3(3 * (sum(n3) % 4))))
    r = int(n3, 3)
    if r > 353:
        rm = min(r, rm)
print(rm)