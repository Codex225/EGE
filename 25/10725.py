from fnmatch import fnmatch
def dels(n):
    r = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return r

for n in range(65001, 1000000):
    if fnmatch(str(n), '6*97*5?'):
        if len([x for x in dels(n) if x % 2 == 0]) >= 4:
            print(n, sum([x for x in dels(n) if x % 2 == 0]))