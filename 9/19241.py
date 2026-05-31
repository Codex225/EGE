q = 0
for r in open("9_19241.txt"):
    res = [int(x) for x in r.strip().split()]
    q += 1
    r3 = [x for x in res if res.count(x) == 3]
    r1 = [x for x in res if res.count(x) == 1]
    if len(r3) == 6 and len(r1) == 1:
        if sum(r3)/len(r3) < r1[0]:
            print(q)