from functools import *
@lru_cache(maxsize=None)
def f(n):
    return 2*(g(n-3) + 8)

@lru_cache(maxsize=None)
def g(n):
    if n < 10:
        return 2 * n
    return g(n - 2) + 1

for n in range(1, 16000):
    g(n)
print(f(15548))