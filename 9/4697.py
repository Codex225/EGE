q = 0
for line in open("9_4697.txt"):
    r = [int(x) for x in line.split()]
    for x in r:
        if r.count(x) == 2 and len(set(r)) == 5 and (x*2 >= ((sum(r) - x*2)/4)):
            q += 1
            break
print(q)
