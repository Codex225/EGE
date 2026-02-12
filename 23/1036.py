def f(s, e):
    if s >= e or s == 10: return s == e
    return f(s + 1, e) + f(s * 2, e)

print(f(1, 30))