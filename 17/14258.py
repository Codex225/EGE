d = [int(x) for x in open("17_14258.txt")]

maxx = max(x for x in d if len(str(abs(x)))==4 and str(x)[-2:] == "22")
res = []
for i in range(2, len(d)):
    x1, x2, x3 = d[i - 2], d[i - 1], d[i]
    r = set()
    for x in x1, x2, x3:
        r.add(len(str(abs(x))))
    if len(r) == 3 and x1 + x2 + x3 >= maxx:
        res.append(x1 + x2 + x3)
print(len(res), max(res))