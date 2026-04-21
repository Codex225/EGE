from re import finditer
f = open("24_1205.txt")
s = f.read().strip()
print(s)
res = []
reg = r"[^GWP]+"
for s1 in finditer(reg, s):
    res.append(len(s1[0]))
print(max(res))
