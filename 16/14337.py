from functools import *
@lru_cache(maxsize=None)
def f(n):
    if n == 1:
        return 1
    return 2 * n + f(n - 1)

for n in range(1, 57694):
    f(n)
a = f(57693)
print(sum([int(x) for x in str(a)]) ** 2)