from re import *
s = next(open("24_12254.txt")).strip()
pat = r"(SQ|Q)?((RSQ)+)(RS|R)?"
reg = rf"(?=({pat}))"
res = []
for s1 in finditer(reg, s):
    res += [len(s1[1])]

print(max(res))