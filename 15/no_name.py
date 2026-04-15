for x in range(0, 100_000):
    for y in range (0, 100_000):
        if 3 *y + 2 *x  == 123456:
            print(x, y)
            break












# def f(x):
#     p = 81 <= x <= 110
#     q = 85 <= x <= 95
#     a = a1< x <= a2
#     return ((not a) <= p) <= (a <= q)
#
# d = [81, 110, 85, 95]
# dots =[]
# for x in d:
#     dots.append(x - 0.1)
#     dots.append(x + 0.1)
#     dots.append(x)
# res = []
# for a1 in dots:
#     for a2 in dots:
#         if a2>= a1 and all([f(x) for x in dots]):
#             res.append(round(a2 - a1))
# print(max(res))