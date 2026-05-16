f = open("26_10133.txt")
n = int(f.readline())
timeline = [0] * 100_000
for l in f:
    st, en = [int(el) for el in l.split()]
    for t in range(st, en):
        timeline[t] +=1
mx = max(timeline)
m = c = 0
for t in range(len(timeline)):
    if timeline[t] > 0:
        c += 1
        m = max(m, c)
    else:
        c = 0
print(max(timeline), m)