for n in range(1, 1000):
    nbin = bin(n)[2:]
    if nbin.count("1") % 2 == 0:
        nbin = nbin + "0"
        nbin = "10" + nbin[2:]
    else:
        nbin = nbin + "1"
        nbin = "11" + nbin[2:]
    r = int(nbin, 2)
    if r >= 16:
        print(n)
        break