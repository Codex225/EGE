s = open("24_1866.txt").readline()
m = 0
for i in range(len(s)):
    for j in range(i + m, len(s)):
        str = s[i: j]
        if "ad" not in str and "da" not in str:
            m = max(m, len(str))
        else:
            break
print(m)
#3146
# s = open("24_1866.txt").readline()
# s = s.replace("da", "d a").replace("ad", "a d")
# print(max(map(len, s.split())))
