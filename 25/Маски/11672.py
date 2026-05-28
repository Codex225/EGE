from fnmatch import fnmatch
def prov(n):
    x = str(n)

    if len(x)% 2 == 0:
        if len([a for a in x if a in "02468"]) == len(x)//2:
            return True
    return False


for n in range(21025, 10**10 + 1, 21025):
    if fnmatch(str(n), "12*34?5") and prov(n):
        print(n, n // 21025)