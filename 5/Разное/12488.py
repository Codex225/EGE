maxr = -1000000000
for n in range(1, 1000):
    nbin = bin(n)[2:]
    if nbin.count("1") % 2 == 0:
        nbin = "11" + nbin[2:] + "0"
    else:
        nbin = "10" + nbin[2:] + "1"
    r = int(nbin, 2)
    if n < 50:
        maxr = max(maxr, r)
print(maxr)