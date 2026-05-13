def f4(n):
    res = ""
    while n:
        res += str(n % 4)
        n //= 4
    return res[::-1]


for n in range(1, 12000, 2):
    n4 = f4(n)
    if n % 3 == 0:
        n4 = n4[-1] + n4[1:-1] + n4[0] + "1"
    else:
        n4 = n4 + str(n % 3)
    r = int(n4, 4)
    if r <= 340:
        print(r)