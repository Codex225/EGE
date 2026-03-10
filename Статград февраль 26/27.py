from math import *

def d(c1, c2):
    res = []
    for p1 in c1:
        for p2 in c2:
            res.append([dist(p1, p2), p1, p2])
    return max(res)

a = [[float(x) for x in l.split()] for l in open("27_a.txt")]
c = []
while a:
    c += [[a.pop()]]
    for p1 in c[-1]:
        for p2 in a:
            if dist(p1, p2) < 1:
                c[-1].append(p2)
                a.remove(p2)

ds = d(c[0], c[1])[1:]
print(int(abs(ds[0][0] - ds[1][0]) * 1000))
print(int(abs(ds[0][1] + ds[1][1]) * 1000))
#print(len(c), [len(cl) for cl in c])