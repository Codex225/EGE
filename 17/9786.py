d = [int(x) for x in open("17_9786.txt")]

maxx = max([x for x in d if abs(x)>9 and str(x)[-2:] == "25"])
print(maxx)

def prov(x, y, z):
    f = ((len(str(abs(x))) == 4) + (len(str(abs(y))) == 4) + (len(str(abs(z))) == 4)) <= 2 and x + y + z <= maxx
    return f

res = []
for i in range(2, len(d)):
    x1, x2, x3 = d[i - 2], d[i - 1], d[i]
    temp = 0
    for x in [x1, x2, x3]:
        if len(str(abs(x))) == 4:
            temp += 1
    if temp <= 2:
        if x1 + x2 + x3 <= maxx:
            res.append(x1 + x2 + x3)
    # if prov(d[i-2], d[i - 1], d[i]):
    #     res.append(d[i-2] + d[i - 1] + d[i])

print(len(res), max(res))