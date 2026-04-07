f = open("26_8512.txt")
k = int(f.readline())
n = f.readline()
data = []
cells = [-1] * k
for s in f:
    start, end = [int(i) for i in s.split()]
    data.append([start, end])
data.sort()
print(data)
last = -1
count = 0
for passenger in data:
    for i in range(len(cells)):
        if passenger[0] > cells[i]:
            cells[i] = passenger[1]
            count += 1
            last = i
            break
print(count, last + 1)