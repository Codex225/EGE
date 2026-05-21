d = [int(x) for x in open("17_18582.txt")]

dmin = str(min(d))[-1]
res = []
for i in range(2, len(d)):
    x1, x2, x3 = d[i- 2], d[i - 1], d[i]
    q = 0
    for x in x1, x2, x3:
        if x < 0:
            q += 1
    if q >= 2:
        if str(x1 + x2 + x3)[-1] == dmin:
            res.append(abs(x1 + x2 + x3))

print(len(res), max(res))