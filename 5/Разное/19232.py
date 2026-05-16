def f15(n):
    res = []
    while n:
        res.append(n % 15)
        n //= 15
    return res[::-1]

def f10(n):
    k = n[::-1]
    d10=0
    for i in range(0, len(k)):
        d10 += k[i] * 15**i
    return d10
minr = 10000000
for n in range(15, 1000):
    n15 = f15(n)
    if n % 15 == 0:
        n15 = n15 + [n15[0]] + [n15[1]]
    else:
        n15 = n15 + f15((n % 15) * 13)
    print(n15)
    r = f10(n15)
    print(r)

    if r > 700:
        minr = min(minr, r)
print(minr)