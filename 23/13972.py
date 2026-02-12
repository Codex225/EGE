def f(s, e, p):

    if s == e:
        return 1
    elif s > e:
        return 0
    if p == 0:
        return f(s + 2, e, 1)  + f(s * 2, e, 3)
    else:
        return f(s + 2, e, 1) + f(s + 5, e, 2) + f(s * 2, e, 3)

print(f(7, 23, 0) * f(23, 35, 1))