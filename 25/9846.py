from fnmatch import fnmatch


for n in range(2025, 10**8 + 1, 2025):
    if fnmatch(str(n), '12*34?5'):
        print(n, n // 2025)