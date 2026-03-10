f = open("26.txt")
n = int(f.readline())

a = sorted(int(x) for x in f)[:: - 1]
s = l = 0
res = []
for r in range(1, n):
    if a[r - 1] - a[r] > 75:
        l = r
        s = 0
    elif a[r - 1] - a[r] > 48:
        s += 1
    while s > 10:
        if a[l] - a[l + 1] > 48:
            s -= 1
        l += 1
    res.append([r - l + 1, a[r]])
print(*max(res))
