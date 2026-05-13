for p in range(2, 38):
    for s in range(2, 36):
        if (ord("r") - 96+ 9)*(p-1)  + 4 + 11*(s+2) + (ord("t")-96 + 9)*p**4 + 3*p**3 + (ord("n") - 96 + 9)*p**2 + (ord("k") - 96 + 9)*p**1 + 4 == 23593399:
            print(p, s, p*s)