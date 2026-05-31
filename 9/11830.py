q = 0
for r in open("9_11830.txt"):
    res = [int(x) for x in r.strip().split()]
    r2 = [x for x in res if res.count(x)== 2]
    r1 = [x for x in res if res.count(x)==1]
    if len(r2) == 4 and len(r1) == 3:
        pp = 1
        for x in r2:
            pp *= x
        pn = 1
        for x in r1:
            pn *= x
        if pp > 2 * pn:
            q = q + 1
print(q)