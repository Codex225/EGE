d = [int(x) for x in open("17_17680.txt")]

mp = min([x for x in d if x > 0 and x % 41 == 0])
print(mp)
q = 0
res = []
for i in range(1, len(d)):
    if d[i - 1] != d[i] and abs(d[i - 1] - d[i]) % mp == 0:
        res.append(d[i - 1] + d[i])

print(len(res), max(res))