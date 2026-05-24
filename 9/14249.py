q = 0
for r in open("9_14249.txt"):
    res = list(map(int, r.split()))
    q += 1
    res.sort()
    rch = len([x for x in res if x % 2 == 0]) == 3
    summs = (res[0] + res[5]) == (res[1] + res[4]) == (res[2] + res[3])
    if rch and summs:
        print(q)
