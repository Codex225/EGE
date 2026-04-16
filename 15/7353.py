def d(n, m):
    return n % m == 0

def f(x, a):

    B = 70 <= x <= 80
    return d(x, a) or (B <= (not d(x, 18)))

k = 0
for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        k += 1
print(k)