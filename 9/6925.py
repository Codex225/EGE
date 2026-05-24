q = 0
for r in open("9_6925.txt"):
    res = [int(x) for x in r.split()]
    r2 = [x for x in res if res.count(x) == 2]
    rost = [x for x in res if res.count(x) == 1]
    rn = [x for x in res if res.count(x) == 1]
    ch = [x for x in res if x %2 == 0]
    nech = [x for x in res if x % 2 == 1]
    if len(ch) == 0:
        srch = 0
    else:
        srch = sum(ch) / len(ch)
    if len(nech) == 0:
        srnech = 0
    else:
        srnech = sum(nech) / len(nech)
    if (len(r2) == 2 and len(rost) == 4) + (abs(srch - srnech) > 50) == 1:
            q += 1
print(q)