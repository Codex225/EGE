
def fact(n):
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)
    return res

print(fact(1000))
def prov(res):
    for num in res:
        if "3" not in str(num):
            return False
    return True

print(prov([13, 3, 43]))
for n in range(1_379_210 + 1, 1_381_310):
    res = fact(n)
    if len(res) == 5 and prov(res) == True:
        print(n, max(res))
