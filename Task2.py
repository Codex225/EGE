from functools import *

@lru_cache(maxsize=None)
def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        return f(start + 1, end) + f(start * 3, end) + f(start + start - 1, end)

print(f(2, 27))