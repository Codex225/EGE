f = open("26_9793.txt")

n = int(f.readline())
data = []
num = 0
for s in f:
    shlif, okr = [int(x) for x in s.split()]
    num += 1
    if shlif < okr:
        data.append([shlif, "s", num])
    else:
        data.append([okr, "o", num])
data.sort()
print(data)
lenta = [0] * n
k1 = 0
k2 = -1
last = 0
for x in data:
    if x[1] == "s":
        lenta[k1] = x[2]
        k1 += 1

    else:
        lenta[k2] = x[2]
        k2 -= 1
    last = x
print(last[2])
if last[1] == "s":
    print(k1 - 1)
else:
    print(k1)