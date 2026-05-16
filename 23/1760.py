def f(s, e, a, b):
    if s == 13:
        a = 1
    if s == 17:
        b = 1
    if a + b == 2:

        return 0
    if s > e: return 0
    if s == e and a + b == 1: return 1

    return f(s + 2, e, a, b) + f(s + 3, e, a, b) + f(s + 5, e, a , b)

print(f(5, 25, 0, 0 ))