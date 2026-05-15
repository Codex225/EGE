def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return f(n - 1) + f(n - 2) + 1
    else:
        return g(n - 3)

def g(n):
    if n > 100:
        return n
    return g(n + 2) + 1

print(f(15) + f(12))
