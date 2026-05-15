nmax = -111111111111111
for n in range(1, 1000):
    nbin = bin(n)[2:]
    if n % 2 == 0:
        nbin = nbin + "1"
    else:
        nbin = nbin + "0"
    if int(nbin, 2) % 2 == 0:
        nbin = nbin + "1"
    else:
        nbin = nbin + "0"
    res = int(nbin, 2)
    if res < 171:
        nmax = max(nmax, n)
print(nmax)