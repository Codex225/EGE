from fnmatch import fnmatch

for n in range(2025, 10**10 +1, 2025):
    if len(str(n)) >= 8:
        if str(n)[:2] == "43" and str(n)[-5:] == "13450":
            if str(n)[-6] in "0123456789" :
                if set(str(n)[2:-6]) <= set("13579"):
                    print(n, n // 2025)