for n in range(1, 1000):
    nbin = bin(n)[2:]
    nbin = nbin + nbin[-1]
    if nbin.count('1') % 2 == 0:
        nbin = nbin + "0"
    else:
        nbin = nbin + "1"
    if nbin.count('1') % 2 == 0:
        nbin = nbin + "0"
    else:
        nbin = nbin + "1"
    r = int(nbin, 2)
    if r > 114:
        print(r)
        break
