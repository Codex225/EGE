from functools import *
@lru_cache(maxsize=None)
def f(n):
    if n <= 7:
        return n
    return g(n - 3) * 3
@lru_cache(maxsize=None)
def g(n):
    if n <= 7:
        return n
    return g(n - 1) + 4

for n in range(1, 43001):
    f(n)
print(f(43000))