from fnmatch import fnmatch
def dels(n):
    dn = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dn.add(i)
            dn.add(n // i)
    return dn

for n in range(100_000, 200_000 + 1):
    r = [x for x in dels(n) if x%2==1 and fnmatch(str(x), "?1*")]
    if len(r) > 8:
        print(n, sum(r))