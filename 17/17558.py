d = [int(x) for x in open("17_17558.txt")]

kr = len([n for n in d if n % 32 == 0])
res = []
for i in range(1, len(d)):
    x1, x2 = d[i-1], d[i]
    if any([a < 0 for a in (x1, x2)]) and x1 + x2  < kr:
        res.append(x1 + x2)
print(len(res), max(res))