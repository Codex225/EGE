from functools import *

@lru_cache(maxsize=None)
def f(n):
    if n < 5:
        return n
    return 2*n * f(n - 4)

for n in range(1, 13768):
    f(n)
print((f(13766) - 9 * f(13762)) // f(13758))