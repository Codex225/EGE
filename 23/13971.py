from functools import *
res = set()
@lru_cache(maxsize=None)
def f(n, q):
    if q == 7:
        return res.add(n)
    f(n + 7, q + 1)
    f(n + 5, q + 1)
    f(n - 3, q + 1)
