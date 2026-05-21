d = [int(x) for x in open("17_14256.txt")]
resv = [x for x in d if str(x)[-2:] == "25"]
print(resv)
mmax = max(resv)

res = []
for i in range(2, len(d)):
    x1, x2, x3 = d[i-2], d[i-1], d[i]
    q = 0
    for x in (x1, x2, x3):

        if sum([int(a) for a in str(abs(x))]) % 2 == 1:
            q += 1
    if q >= 2:
        if x1 + x2 + x3 <= mmax:
            res.append(x1 + x2 + x3)
print(len(res), max(res))

