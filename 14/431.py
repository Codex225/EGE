def f7(n):
    res = []
    while n:
        res.append(n % 7)
        n //= 7
    return res[::-1]

for x in range(1, 10):
    n = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 7**(2*x)
    n7 = f7(n)
    if sum(n7) == 18:
        print(x, n)
        break