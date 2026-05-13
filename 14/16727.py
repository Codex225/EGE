def f27(n):
    res = []
    while n:
        res.append(n % 27)
        n //= 27
    return res[::-1]

n = 5*729**2024 + 3*243**1413 - 7 * 81**169 - 2*9**107 + 3017
n27 = f27(n)
s = 0
for x in n27:
    if x <= 25:
        s += x
print(s)
