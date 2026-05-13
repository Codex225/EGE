def f6(x):
    res = []
    while x != 0:
        res.append(x % 6)
        x = x // 6
    return res[::-1]


for x in range(1, 2030):
    d = 6**260 + 6**160 + 6**60 - x
    k0 = len([a for a in f6(d) if a == 0])
    if k0 == 202:
        print(x)
        break
