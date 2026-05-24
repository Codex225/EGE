q = 0
for line in open("9_18943.txt"):
    r = [int(x) for x in line.split()]
    r3 = [x for x in r if r.count(x) == 3]
    r2 = [x for x in r if r.count(x) == 2]
    r = [x for x in r if r.count(x) == 1]
    if r3 and r2 and r and r3[0] + r2[0] >= sum(r):
        q += 1
print(q)