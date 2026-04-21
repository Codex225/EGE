from re import *
s = next(open("24_20813.txt")).strip()
pat = r"([789][0789]*|[0])([-*]([789][0789]*|[0]))+"
reg = rf"(?=({pat}))"
res = []
for s1 in finditer(reg, s):
    res += [len(s1[1])]

print(max(res))