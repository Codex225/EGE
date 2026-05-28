from fnmatch import *

for i in range(23, 10 ** 9 + 1, 23):
    if fnmatch(str(i), "12345?7?8"):
        print(i, i // 23)