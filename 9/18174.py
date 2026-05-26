q = 0

for r in open("9_18174.txt"):
    res=[int(x) for x in r.strip().split()]

    r2 = [x for x in res if res.count(x) == 2]
    r = [x for x in res if res.count(x) == 1]
    plus = [x for x in res if x > 0]
    minus = [x for x in res if x <0]
    if len(r2) == 2 and len(r) == 4 and abs(sum(minus)) > sum(plus):
        q += 1
print(q)