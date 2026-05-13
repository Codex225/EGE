def f8(n):
    res = ""
    while n:
        res += str(n % 8)
        n //= 8
    return res[::-1]
rm = 0
for n in range(1, 10000):
    n8 = f8(n)
    if n % 2 == 0:
        n80 = n8 + str(f8(max([int(x) for x in n8])))
    else:
        n80 = n8 + str(f8(2*min([int(x) for x in n8])))
    r = int(n80, 8)
    if r < 313:
        rm = max(r, rm)
    if r == 310:
        print(n)
print(rm)