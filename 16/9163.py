from functools import *

@lru_cache(maxsize=None)
def f(n):
    if n >= 2025:
        return n
    return f(n + 1) - f(n + 2) + 7

for n in range(2100, 1, -1):
    f(n)

print(f(15) - f(24))