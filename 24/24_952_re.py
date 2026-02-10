from re import*
f = open("24_952.txt")
s = f.readline().strip()
#reg = r"[0-9BCDF]+"
reg = r"[^AE]+"
res = []
for s1 in finditer(reg, s):
    res.append(len(s1[0]))
print(max(res))