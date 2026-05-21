d = [int(x) for x in open("17_14257.txt")]

max5 = max(x for x in d if len(str(abs(x))) == 5 and str(x)[-1] == "7")
print(max5)
res = []
for i in range(2, len(d)):
    x1, x2, x3 = d[i], d[i-1], d[i-2]
    if ((x1 + x2 + x3) <= max5) and ((str(x1)[-2:] == "12") + (str(x2)[-2:] == "12") + (str(x3)[-2:] == "12") == 2):
        res.append(x1 + x2 + x3)
print(len(res), min(res))