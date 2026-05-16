def f(a, b):
    if a< b or a == 35:
        return 0
    if a == b:
        return 1
    return f(a // 3, b) + f(a - 2, b) + f(a - 5, b)

print(f(41, 37) * f(37, 8))