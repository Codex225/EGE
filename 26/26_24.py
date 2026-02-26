f = open("26_24.txt", "r")

S, N = [int(x) for x in f.readline().split()]
data = sorted([int(x) for x in f])
#print(data)
razm = S
a = []
for x in data:
    if S - x >= 0:
        S = S - x
        a.append(x)
print(len(a))
b = a[:-1] #минимальные файлы без последнего
data.reverse()
summm = sum(b)
for x in data:
    if x + summm <= razm:
        print(x)
        break
