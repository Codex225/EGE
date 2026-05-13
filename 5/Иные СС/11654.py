def f7(n):
    res = ""
    while n:
        res += str(n % 7)
        n //= 7
    return res[::-1]

for n in range(1, 10000):
    n7 = f7(n)
    if n7.count('2') % 2 == 0:
        n7 = n7 + "555"
    else:
        n7 ="1" + n7
    r = int(n7, 7)
    if r < 3799:
        print(n)