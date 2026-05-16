from functools import *
res = set()
@lru_cache(maxsize=None)
def f(a, q):
    if q == 68:
        return res.add(a)
    f(a + 3, q + 1)
    f(a - 2, q + 1)

f(1, 0)
print(len(res))