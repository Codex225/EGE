c = 0

for i in open("9_17628.txt"):
    ds = [int(x) for x in i.split()]
    if max(ds) + min(ds) <= sum(ds) - min(ds) - max(ds):
        c += 1
print(c)