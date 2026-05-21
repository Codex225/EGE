d = [int(x) for x in open("17_11703.txt")]

k = max([x for x in d if str(x)[-2:] == "18"])
res = []
for i in range(2, len(d)):
    x1, x2, x3 = d[i], d[i - 1], d[i - 2]
    pr = [x for x in (x1, x2, x3) if len(str(abs(x))) == 5 and x1 * x2 * x3 % k == 0]
    if len(pr) >= 1:
        res.append(x1 * x2 * x3)
print(len(res), max(res))