def f(a, b):
    if a < b or a == 32:
        return 0
    if a == b:
        return 1
    return f(a - 1, b) + f(a - 5, b)

print(f(42, 23) * f(23, 22) * f(22, 9))