q = 0
def prov(re):
    re.sort()
    print(re)
    a = re[1] - re[0]
    flag = True
    for i in range(1, len(re)):
        if re[i] - re[i - 1] != a:
            flag = False
            break
    return flag


for r in open("9_5627.txt"):
    res = [int(x) for x in r.strip().split()]
    rp = [x for x in res if res.count(x) > 1]
    if len(rp) or prov(res):
        q += 1

print(q)
