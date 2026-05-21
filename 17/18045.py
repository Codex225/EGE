d = [int(x) for x in open("17_18045.txt")]

q2 = 0
for x in d:
    if 10 <= x <= 99:
        q2 += 1
res = []
for i in range(1, len(d)):
    x1, x2 = d[i-1], d[i]
    if x1 % 10 + x2 % 10 == q2:
        res.append(x1 + x2)
print(len(res), min(res))