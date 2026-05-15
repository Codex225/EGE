from functools import *
@lru_cache(maxsize=None)
def f(n):
    if n <= 3:
        return n + 3
    if f(n - 1) % 2 == 0:
        return f(n - 2) + n
    return f(n - 2) + 2 * n

for n in range(1, 100):
    f(n)

sum = 0
for n in range(40, 51):
    sum += f(n)
print(sum)