from functools import *

@lru_cache(maxsize=None)
def f(x, end):
    if x < end:
        return 0
    elif x == end:
        return 1
    else:
        return f(x - 1, end) + f(x - 2, end) + f(x - 3, end)

print(f(68, 30))