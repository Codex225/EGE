def f15(n):
    s = []
    while n:
        s.append(n % 15)
        n //= 15
    return s[::-1]

n = 11*15**65 + 18*15**38 - 124*15**17 + 19 * 15**11 + 18338
print(len(set(f15(n))))