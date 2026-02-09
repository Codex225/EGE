f = open("24_3019.txt")
s = f.readline().strip()
count = 0
#print(len(s))
for i in range(len(s)):
    for j in range(i, len(s)):
        str = s[i:j + 1]
        if len(str) <= 15 and str[0] == "A" and "F" in str and str[-1] == "B" and "A" not in str[1:-1]  \
                and "B" not in str[1:-1]:

            count += 1
        elif len(str) > 15 or str[0] != "A"  or "A" in str[1:-1] or "B" in str[1:-1]:
             break
    if i % 10_000 == 0:
        print(i)

print(count)