from functools import lru_cache

@lru_cache(None)
def f(n):
    return 2*(g(n - 3) + 8)

@lru_cache(None)
def g(n):
    if n < 10:
        return 2 * n
    return g(n - 2) + 1

for x in range(0, 20000):
    f(x)
print(f(15548))



# @lru_cache(None)
# def f(n):
#     if n < 11:
#         return n
#     return n + f(n - 1)
#
# for n in range(1, 2100):
#     f(n)
#
# print(f(2024) - f(2021))
# # f = {}
# for n in range(1, 2100):
#     if n < 11:
#         f[n] = n
#     if n >= 11:
#         f[n] = n + f[n - 1]
# print(f[2024] - f[2021])

