from re import *
s = next(open("24_22359.txt")).strip()
pat = r"[1-9ABCDE][0-9ABCDE]*[05A]"
reg = rf"(?=({pat}))"
res = []
for s1 in finditer(reg, s):
    #print(s1)
    res += [len(s1[1])]
    if len(s1[1]) == 112:
        print(s1.start()+ 112 - 1, s1[1])

print(max(res))