q = 0
s = 0
for r in open("9_13824.txt"):
    res = [int(x) for x in r.split()]
    q += 1
    rchet = "".join([str(x % 2) for x in res])
    #print(rchet)
    rchetre = (rchet == "1010101") or (rchet == "0101010")
    rpovt = [x for x in res if res.count(x) >=2]
    rnepovt = [x for x in res if res.count(x) == 1]
    pp = 1
    for n in rpovt:
        pp = pp * n
    #print(pp)
    if len(rpovt) == 0: pp = 0
    ppn = 0
    for n in rnepovt:
        ppn = ppn + n
    #print(ppn)
    if ppn * 3 >= pp and rchetre:
        s = s + q
print(s)

