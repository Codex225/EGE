a = [int(x) for x in open("17_1970.txt")]
res = []

for i in range(len(a) - 1):
    if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
        res.append(a[i] + a[i + 1])
print(len(res), max(res))