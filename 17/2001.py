a = [int(x) for x in open("17_2001.txt")]
res = []

for i in range(len(a) - 3):
    tl = [str(a[j] % 2) for j in range(i, i + 4)]

    if "".join(tl) == "0101" or "".join(tl) == "1010":
        res.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3])

print(len(res), max(res))