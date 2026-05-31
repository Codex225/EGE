from fnmatch import fnmatch

def s(n):
    return sum([int(x) for x in str(n)])

for n in range(86513, 10**12 + 1, 86513):
    if fnmatch(str(n), '17*46??8') and s(n) ** 0.5 == int(s(n) ** 0.5):
        print(n, n // 86513)