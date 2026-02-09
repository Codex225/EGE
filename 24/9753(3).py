f = open("24_9753.txt")
s = f.readline().strip()
k = 0
print(len(s))
for i in range(len(s)):
    for j in range(i + k, len(s)):
        str = s[i:j]
        if str.count("Y") == 150:
            k = max(k, len(str))
        elif str.count("Y") > 150:
            break
##    if i%10000==0:
##        print(i, "i")
print(k)

