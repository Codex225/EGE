def f12(n):
    res = []
    while n:
        res.append(n % 12)
        n = n // 12
    for i in range(len(res)):
        if res[i] == 10:
            res[i] == "a"
        if res[i] == 11:
            res[i] == "b"
    return "".join(map(str, res))[::-1]

for n in range(1, 1000):
    n12 = f12(n)
    if n % 3 == 0:
        n12 = "1" + n12 + "b"
    else:
        n12 = "2" + n12 + "0"
    r = int(n12, 12)
    if r < 1996:
        print(r)



