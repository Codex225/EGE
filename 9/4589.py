q = 0
for line in open("9_4589.txt"):
    r = [int(x) for x in line.strip().split()]
    r.sort()
    if max(r) < (sum(r) - max(r)) and ((r[0] + r[3]) == (r[1] + r[2])):
        q += 1
print(q)