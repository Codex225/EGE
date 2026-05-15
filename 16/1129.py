
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return f(n//2) + 1
    return f(n - 1) + n

q = 0
for n in range(1, 100_000):
    if f(n) == 16:
        q += 1
print(q)
