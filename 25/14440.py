from fnmatch import fnmatch

def dels(n):
    r = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)
    return r
def pr(n):
    s = 1
    for x in str(n):
        s *= int(x)
    return s

for n in range(2, 10**7 +1):
    if len(dels(n)) == 0 and fnmatch(str(n), '31*567?'):
        print(n, pr(n))

#медленно, рисковано