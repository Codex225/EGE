def sumd(x):
    return sum([int(a) for a in str(x).split()]) % 2 == 0
q = 0
for r in open("9_18258.txt"):
    res = [int(x) for x in r.strip().split()]
    q += 1
    rp = [x for x in res if res.count(x) > 1]
    if res == sorted(res):
        if len(rp) > 0 and any(sumd(x) for x in res):
            print(q)

