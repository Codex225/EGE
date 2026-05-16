def f(s, e):
    if s > 20 or s == 11: return 0
    if s == 20: return 1
    return f(s + 1, e) + f(s * 2, e) + f(s ** 2, e)

print(f(2, 20))