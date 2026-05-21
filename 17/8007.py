f = open("17_8007.txt")
d = [int(x) for x in open("17_8007.txt")]
r = [x.strip() for x in open("17_8007.txt")]
s = "".join(r)
summ = sum(int(x) for x in s)
res = []
for i in range(len(d) - 1):
    x1, x2 = d[i - 1], d[i]
    if (str(x1)[-2:] == "10") + (str(x2)[-2:] == "10")  == 1 and (x1 + x2) < summ:
        res.append(x1 + x2)
print(len(res), min(res))
