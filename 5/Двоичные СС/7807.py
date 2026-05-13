mr = 0
for n in range(1, 1000000):
    nbin = bin(n)[2:]
    if n % 3 == 0:
        nbin = nbin + nbin[:2]
    else:
        nbin = nbin + bin(n % 3)[2:]
    r = int(nbin, 2)
    if r < 105:
        mr = max(mr, r)
    if r == 99:
        print(n)
#print(mr)