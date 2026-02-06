f = open("24_16789.txt")
s = f.readline().strip()

m_ = 20000

for i in range(len(s)):
    for j in range(i + m_, i, - 1):
        str = s[i:j]
        if str.count("D") >= 300 and "E" not in str:
            m_ = min(m_, len(str))
        elif str.count("D") < 300:
            break
    if i % 10000 == 0:
        print(i)
print(m_)
