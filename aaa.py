f = open("9.txt")
strs = []
for s in f:
    strs.append(s.strip().split())
print(strs)
for s in strs:
