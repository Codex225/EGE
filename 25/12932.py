from fnmatch import fnmatch

for n in range(2024, 10**10 + 1, 2024):
    if fnmatch(str(n), "1?2*4") and n**0.5 == int(n**0.5):
        print(n, n // 2024)