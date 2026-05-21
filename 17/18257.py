d = [int(x) for x in open("17_18257.txt")]

maxx = str(max(d))[-1]
res = []
for i in range(1, len(d)):
    if str(i + i + 1)[-1] == maxx:
        res.append(abs(d[i] + d[i - 1] - (i + 1 + i)))
print(len(res), min(res))