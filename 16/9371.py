from functools import *
@lru_cache(None)
def f(n):
    if n >= 3210:
        return 1
    return f(n + 3) + 7

@lru_cache(None)
def g(n):
    if n < 10:
        return n
    return g(n - 3) + 5

for n in range(1, 3300):
    g(n)

for n in range(3300, 1, -1):
    f(n)
print(f(15) - g(3000))