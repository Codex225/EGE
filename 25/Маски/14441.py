from fnmatch import fnmatch

def dels(n):
    r = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)
    return sum(r)

for n in range(2068, 10**9 +1, 2068):
    ss = dels(n)
    if fnmatch(str(n), "193*7?") and ss % 7 == 0:
        print(n, ss)
#долго работает