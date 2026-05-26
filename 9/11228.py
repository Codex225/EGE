s = 0
for r in open("9_11228.txt"):
    res = [int(x) for x in r.strip().split()]
    r3 = [x for x in res if res.count(x) == 3]
    r2 = [x for x in res if res.count(x) == 2]
    res.sort()
    if len(r3) == 3 and len(r2) == 4:
        if sum(x % 2 for x in res[:4]) == 2:
            s = s+sum(res)
print(s)