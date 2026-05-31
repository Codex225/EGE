q = 0
for r in open("9_2929.txt"):
    res = [int(x) for x in r.split()]
    res.sort()
    if (max(res) + min(res)) / 2 <= res[1]:
        q += 1
print(q)