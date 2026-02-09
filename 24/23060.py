f = open("24_23060.txt")
s = f.readline().strip()

m = 10000
#print(s)
for i in range(len(s)):
    for j in range(i + m, i, -1):
        str = s[i:j]
        if str.count("TYZUX") == 78 and str[0] != "T" and str[-1] != "X":
            m = min(m, len(str))

        elif str.count("TYZUX") < 78 or str[0] == "T" and str[-1] == "X":
            break
    if i % 10000 == 0:
        print(i)
print(m)