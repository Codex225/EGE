q = 0
for r in open("9_14253.txt"):
    res = [int(x) for x in r.split()]
    r2 = [x for x in res if res.count(x) == 2]
    r1 = [x for x in res if res.count(x) == 1]
    if len(r2) == 6 and len(r1) == 1 or  (sum(res) / len(res))** 0.5 == int(    (sum(res) / len(res)) ** 0.5)  :
            q += 1
print(q)
