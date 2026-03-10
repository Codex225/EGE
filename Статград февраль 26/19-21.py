# def f(a, b, m):
#     if a * b >= 415:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a + 3, b, m - 1), f(a, b + 3, m - 1), f(a + 17, b, m - 1), f(a, b + 17, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else any(h)
#
# print(len([s for s in range(1, 52) if f(8, s, 2)]))


def f(a, b, m):
    if a * b >= 415:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 3, b, m - 1), f(a, b + 3, m - 1), f(a + 17, b, m - 1), f(a, b + 17, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print([s for s in range(1, 52) if f(8, s, 3) > f(8, s, 1)])
print([s for s in range(1, 52) if f(8, s, 4) > f(8, s, 2)])
