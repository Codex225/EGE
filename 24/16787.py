s = next(open("24_16787.txt"))
#print(s)
min_ = 10000
for i in range(len(s)):
    for j in range(i + min_, i, -1):
        str = s[i:j]
        if str.count('A') >= 305:
            min_ = min(min_, len(str))
        else:
            break
    if i % 10000 == 0:
        print(i)
print(min_, "min")


