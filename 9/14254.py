q = 0
for r in open("9_14254.txt"):
    res = [int(x) for x in r.split()]
    rpov = [x for x in res if res.count(x) >= 2]
    rnep = [x for x in res if res.count(x) == 1]
    if (sum(rnep) <= sum(rpov)) + ((max(res) * min(res)) < 3*(sum(res) - max(res) - min(res))) == 1:
        q += 1
print(q)