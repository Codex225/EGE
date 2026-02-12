def f(s, e, p1, p2):
    if s == 20:
        p1 = 1
    if s == 30:
        p2 = 1
    if s > e: return 0
    if s == e and p1 + p2 == 1:
        return 1
    return f(s + 3, e, p1, p2) + f(s + 5, e, p1, p2) + f(s * 2, e, p1, p2)


p1 = 0
p2 = 0
print(f(10, 40, p1, p2))