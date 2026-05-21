d = [int(x) for x in open("17_14260.txt")]
pr = []
for x in d:
    if x > 0 and len(str(abs(x))) == 4 and str(x)[-1] == str(x)[-2]:
        pr.append(x)
mplus = min(pr)
res = []
for i in range(2, len(d)):
    x1, x2, x3 = d[i -2], d[i-1], d[i]
    q = 0
    for x in x1, x2, x3:
        if 100 <= abs(x) < 1000:
            q += 1
    if q == 3 and x1 + x2 + x3 > mplus:
        res.append(x1 + x2 + x3)
print(len(res), max(res))