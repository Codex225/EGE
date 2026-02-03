f = open("24_17535.txt")
s = f.readline().strip()
print(len(s))
m = 0
#s.replace("CD", "X")
for i in range(len(s)):
    for j in range(i + m, len(s)):
        str = s[i: j + 1]
        if str.count("CD") == 160:
            m = max(m, len(str))
        elif str.count("CD") > 160:
            break
    if i % 10000 == 0:
        print(i, "i")
print(m)