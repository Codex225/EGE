d = [int(x) for x in open("17_14259.txt")]
summ11 = 0
for x in d:
    if str(x)[-3:] == "111":
        summ11 += x
res = []
for i in range(2, len(d)):
    x1, x2, x3 = d[i], d[i-1], d[i-2]
    q = 0
    for x in (x1, x2, x3):
        maxx = max(int(n) for n in str(abs(x)))
        if x % maxx == 0:
            q += 1
    if q >= 1 and x1 * x2 * x3 >= summ11:
        res.append(x1 * x2 * x3)
print(len(res), min(res))