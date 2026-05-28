from fnmatch import fnmatch

for n in range(999, 10**9 + 1, 999):
    if fnmatch(str(n), "13???57?9") and n % 999 == 0:
        print(n, n // 999)