def sumch(n):
    sum = 0
    s = [int(x) for x in str(n)]
    for x in s:
        if x % 2 == 0:
            sum += x
    return sum

def sumchm(n):
    sum = 0
    s = [int(x) for x in str(n)]
    for i in range(0, len(s)):
        if i % 2 == 1:
            sum += s[i]
    return sum

for n in range(1, 10000):
    r = abs(sumch(n) - sumchm(n))
    if r == 13:
        print(n)