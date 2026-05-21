d = [int(x) for x in open("17_2002.txt")]

def prov(*xx):
    r = list(xx)
    return (r[3] <= r[2] <= r[1] <= r[0]) and ((max(r) - min(r)) > 1000)
res = []
for i in range(3, len(d)):
    x1, x2, x3, x4 = d[i - 3], d[i - 2], d[i - 1], d[i]
    if prov(x1, x2, x3, x4):
        res.append(x1 + x2 + x3 + x4)
print(len(res), min(res))

