f = open("24_23169.txt")
s = f.readline()

m = 0
for i in range (len(s)):

    for j in range (i + 1 + m, len(s)):
        str = s[i:j]
        q = 0
        for k in str:

            if k in "0123456789":

                q += 1


        if str[0] == "D" and "D" not in str[1:] and q == 50:
           m = max(m, len(str))
        elif str[0] != "D" or "D" in str[1:] or q > 50:
            break

    if i % 10000 == 0:
        print(i)
print(m)
#180

