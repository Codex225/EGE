from string import *

f = open("24_22357.txt", "r")
s = f.readline().strip()

for x in "EFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(x, "*")

m = 1
for i in range(len(s)):
    for j in range(i + m - 1, len(s)):
        str = s[i : j + 1]
        if "*" not in str and str[0] != "0" and int(str, 14) % 2 == 0:
            m = max(m, len(str))
            print(m)
            if len(str) == 112:
                 print(str, i)
        elif str[0] == "0" or "*" in str:
            break
    # if i % 100_000 == 0:
    #     print(i)
#print(m)
# m = 112