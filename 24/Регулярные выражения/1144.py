from re import *

s = next(open("24_1144.txt")).strip()
#reg = r"(A[ABCDEF]F)+"
pat = r"A[ABCDEF]+?F"
reg = rf"(?=({pat}))"
mmin = (10 ** 6 + 1)
for s1 in finditer(reg, s):
    mmin = min(mmin, len(s1[1]))
print(mmin)

