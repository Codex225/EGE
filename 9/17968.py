q = 0
for r in open("9_17968.txt"):
    res = [int(x) for x in r.split()]
    res.sort()
    rch = [x for x in res if x%2 == 0]
    rne = [x for x in res if x%2 == 1]
    if max(res) < (sum(res) - max(res)):
        if sum(rch) == sum(rne):
            q += 1
print(q)

