from functools import *
@lru_cache(None)
def f(n):
    if n > 3000:
        return n
    return (2 * n + 4) * f(n + 2)

for n in range(3100, 1, -1):
    f(n)

a = f(20)//f(28)
print(sum([int(x) for x in str(a)]))