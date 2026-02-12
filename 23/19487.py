def f(s, e, p1 , p2):
    if s == 20:
        p1 = 1
    if s == 30:
        p2 = 1
    if s == e:
        #if p1 == 1 and p2 == 0 or p1 == 0 and p2 == 1 or p1 == 0 and p2 == 0:
        if p1 + p2 < 2:
            return 1
    if s > e:
        return 0
    return f(s + 2, e, p1, p2) + f(s + 3, e, p1, p2) + f(s * 2, e, p1, p2)

print(f(8, 35, 0, 0))