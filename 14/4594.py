def n5(n):
    res = []
    while n:
        res.append(n % 5)
        n //= 5
    return res[::-1]

n = 4*625**1920 + 4*125**1930 - 4*25**1940 - 3*5**1950 - 1960
n5 = n5(n)
print(n5.count(0))