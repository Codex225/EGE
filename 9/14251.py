
for r in open("9_14251.txt"):
    res = [int(x) for x in r.split()]
    r22 = [x for x in res if res.count(x)==2]
    razl = [x for x in res if res.count(x) == 1]
    if len(r22) == 4 and len(razl) == 3:
        if sum(r22) <= sum([x for x in res if x % 2 == 1]):
            print(sum(res))
            break
