f = open("24_3019.txt")
s = f.readline().strip()
print(s)
m = 0
q = 0
for i in range(len(s)):
    for j in range(i + m, len(s)):
        string = s[i, j + 1]
        if len(string) <= 15 and string[0] == "A" and "F" in string and string[-1] == "B" and "A" not in string[1, -1]:
            q = q + 1

print(q)