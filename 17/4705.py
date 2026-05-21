d = [int(x) for x in open("17_4705.txt")]

resp = []
for x in d:
    if str(x)[-1] == "3":
        resp.append(x)
m3 = max(resp) ** 2
res = []
for i in range(len(d)):
    x1, x2 = d[i - 1], d[i]
    if  ((str(x1)[-1] == "3") + (str(x2)[-1] == "3")) == 1 and (x2 ** 2 + x1 ** 2) >= m3:
        res.append(x2 ** 2 + x1 ** 2)

print(len(res), max(res))