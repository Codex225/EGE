from functools import *

@lru_cache(maxsize=None)
def f(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        return f(start + 1, end) + f(start * 5, end)

print(f(3, 30) * f(30, 68))