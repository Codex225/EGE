def f(s, e):
    if s > e: return 0
    if s == e: return 1
    return f(s + 3, e) + f(s + max([int(x) for x in str(s)]),e)

print(f(10, 24) * f(24, 41))