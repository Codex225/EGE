def ss(a, base):
    res = []
    while a != 0:
        res.append(a % base)
        a //= base
    return res[::-1]

res = []
for x in range(11501):
    a = 7**270 + 7 ** 170 + 7 *70 -x
    a7 = ss(a, 7)
    res.append([a7.count(0), x])
res.sort()
print(max(res))