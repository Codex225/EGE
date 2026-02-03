#f = open("24_9753.txt")
#s = f.readline()
s = next(open("24_9753.txt"))
m = 0
for i in range(len(s)):
    for j in range(i + m, len(s)):
        str = s[i:j]
        if str.count("Y") == 150:
            m = max(m, len(str))
        elif str.count("Y") > 150:
            break
    if i % 10000 == 0:
        print(i)
print(m)

