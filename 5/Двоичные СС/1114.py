for n in range(96, 1000):
    nbin = bin(n)[2:]
    if nbin.count('0') == nbin.count('1'):
        nbin = nbin + nbin[-1]
    elif nbin.count('1') > nbin.count('0'):
        nbin = nbin + "0"
    elif nbin.count('1') < nbin.count('0'):
        nbin = nbin + "1"
    if nbin.count('0') == nbin.count('1'):
        nbin = nbin + nbin[-1]
    elif nbin.count('1') > nbin.count('0'):
        nbin = nbin + "0"
    elif nbin.count('1') < nbin.count('0'):
        nbin = nbin + "1"
    if nbin.count('0') == nbin.count('1'):
        nbin = nbin + nbin[-1]
    elif nbin.count('1') > nbin.count('0'):
        nbin = nbin + "0"
    elif nbin.count('1') < nbin.count('0'):
        nbin = nbin + "1"
    r = int(nbin, 2)
    if r % 4 == 0:
        print(n)
        break