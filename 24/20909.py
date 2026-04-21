f = open("24_20909.txt")
s = f.readline().strip()

#s = s.replace("AB", "*")
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        res = s[l:r + 1]
        if res.count("AB") == 100:
            m = max(m, len(res))
        elif res.count("AB") > 100:
            break
print(m)