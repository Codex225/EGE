def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 2, b) + f(a + sum([int(x) for x in str(a)]), b)

print(f(3, 29) * f(29, 68))