s = next(open("24_6734.txt"))

m = 10000
for i in range(len(s)):
    for j in range(i + m, i,  - 1):
        str = s[i:j + 1]
        if str.count('.') == 7:
            if len(str)<m:
                m = min(len(str), m)
        elif str.count('.') < 7:
            break
    # if i % 1000 == 0:
    #     print(i)
print(m)