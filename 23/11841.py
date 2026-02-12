def f(s, e):
    if s <= e or s == 20:
        return s == e
    return f(s - 2, e) + f(s - 3, e) + f(s // 5, e)

print(f(41, 10) * f(10, 5))