from fnmatch import fnmatch

def dels(n):
    r = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)
    return r

for n in range(400_000, 500_000 + 1):
    ss = [d for d in dels(n) if fnmatch(str(d), "*7?")]
    if len(ss) >= 18:
        print(n, sum(ss))
