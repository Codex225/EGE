s = open("24.txt").readline()
d = []
m = l = 0

for r in range(len(s)):
    if s[r] in "0123456789":
        l = r + 1
        d = []
    elif s[r] not in d:
        d.append(s[r])
    if len(set(d)) == 26:
        m = max(m, r - l + 1)

print(m)


# s = open("24.txt").readline()
# m = 0
# for i in range(len(s)):
#     for j in range(i + m, len(s)):
#         c = s[i : j + 1]
#         if any (d in c for d in "0123456789"):
#             break
#         if all( d in c for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#             m = max(m, len(c))
# print(m)