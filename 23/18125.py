def f(s, e):
    if s < 3: return 0
    if s == e: return 1
    return f(s - 4, e) + f(s - 7, e) + f(int(s**0.5), e)

print(f(44, 22) * f(22, 3))