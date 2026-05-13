for n in range(1, 1000):
    nbin = bin(n)[2:]
    if len(nbin) % 2 == 0:
        nbin = nbin[: len(nbin) // 2 ] + "000" + nbin[len(nbin) // 2 :]
    else:
        nbin = "1" + nbin + "01"
    r = int(nbin, 2)
    if r >100:
        print(n)