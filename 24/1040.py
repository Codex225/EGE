f = open("24_1040.txt")
s = f.readline().strip()

m = 0
for i in range(len(s)):
    for j in range(i + m, len(s)):
        str = s[i: j + 1]
        flag = True
        for k in str:
            if not k.isdigit():
                flag = False
        if flag:
            m = max(m, len(str))
        elif not flag:
            break
    if i % 10000 == 0:
        print(i)
print(m)