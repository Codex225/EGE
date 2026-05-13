for n in range(1, 1000):
    nbin = bin(n)[2:]
    if n % 3 == 0:
        nbin = nbin + nbin[-3:]
    else:
        nbin = nbin + bin(3 * (n % 3))[2:]
    r = int(nbin, 2)
    if r < 100:
        print(n)
