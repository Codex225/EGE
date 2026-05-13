def f5(n):
    s = ""
    while n:
        s += str(n%5)
        n //= 5
    return s[::-1]

n = 5**2004 - 5**1016 -25**508 - 5**400 + 25**250 - 27

print(f5(n).count("4"))