from re import *
s = next(open("24_21421.txt")).strip()
pat = r"([1-9AB][0-9AB]*[02468A]|[2468A])"
reg = rf"(?=({pat}))"
res = []
for s1 in finditer(reg, s):
    res += [len(s1[1])]

print(max(res))