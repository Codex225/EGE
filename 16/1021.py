from functools import *
@lru_cache(None)
def f(n):
    if n <= 2:
        return g(n)
    return g(n) + f(n - 2)
@lru_cache(None)
def g(n):
    if n <= 2:
        return n
    return f(n - 1) - g(n - 2)

for n in range(1, 100):
    f(n)
    g(n)
print(g(15))