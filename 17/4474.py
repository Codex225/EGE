d = [int(x) for x in open("17_4474.txt")]
minn = min([x for x in d if x % 103 == 0])

res = []
for i in range(1, len(d)):
    if (d[i - 1]  + d[i]) % 2 == 0 and (d[i - 1] - d[i]) % minn == 0:
        res.append(d[i - 1] + d[i])
print(len(res), max(res))