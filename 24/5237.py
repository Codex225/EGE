f = open("24_5237.txt")
s = f.readline().strip()
m = 0
for i in range(len(s)):
    for j in range(i + m, len(s)):
        str = s[i:j]
        flag = True
        for k in range(1, len(str)):
            if str[k] == str[k-1]:
                flag = False
                break

        if "Z" not in str and flag:
            m = max(m, len(str))
        elif "Z" in str or not flag:
            break

    if i % 10000 == 0:
        print(i)
print(m)

