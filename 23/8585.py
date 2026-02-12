def summ(s):
    return sum([int(x) for x in str(s)])


def f(s, e):
    if s <= e: return s == e
    return f(s - summ(s), e) + f(s // 2, e) + f(s - 1, e)

print(f(40, 25) * f(25, 10))