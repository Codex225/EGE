q = 0
for line in open("9_7611.txt"):
    r = [int(x) for x in line.split()]
    if len(set(r)) == 5 and (max(r) + min(r)) * 2 >= (sum(r) - min(r) - max(r)):
        q += 1
print(q)