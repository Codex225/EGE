def f6(n):
    res = ""
    while n:
        res += str(n % 6)
        n //= 6
    return res[::-1]

mn = 0
for n in range(1, 10000):
    n6 = f6(n) + f6(n)[-1]
    n610 = int(n6, 6)
    n2 = bin(n610)[2:]
    n2 = n2 + n2[-1]
    r = int(n2, 2)
    if r < 344:
        mn = max(mn, r)
    if r == 331:
        print(n)
#print(mn)