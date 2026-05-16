def f3(n):
    res = ""
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

for n in range(1, 1000):
    summ = sum([int(x) for x in f3(n)])
    if summ % 2 == 0:
        n3 = "1" + f3(n) + "2"
    else:
        n3 = "2" + f3(n) + "0"
    r = int(n3, 3)
    if r > 100:
        print(r)