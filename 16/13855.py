from functools import *
@lru_cache(maxsize=None)
def f(n):
    if n >= 7777:
        return n
    return n + 5 + f(n + 5)

for n in range(7800, 1, -1):
    f(n)
print(f(1101) - f(1111) )
