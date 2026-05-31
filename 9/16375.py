q = 0
for r in open("9_16375.txt"):
    res = [int(x) for x in r.split()]
    r2 = [x for x in res if res.count(x) == 2]
    r1 = [x for x in res if res.count(x) == 1]
    r1.sort()
    if len(r2) == 2 and len(r1) == 5:
        if r2[0] ** 2 < r1[0] * r1[1] * r1[2]:
            q += 1
print(q)