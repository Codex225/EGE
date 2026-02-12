def f(s, e, n):
    if s == e:
        if n == 3:
            return 0
        else:
            return 1
    elif s > e:
        return 0
    return f(s + 2, e, 1) + f(s + 5, e, 2) + f(s ** 2, e, 3)

print(f(4, 36, 0))