for n in range(256):
    nbin8 = "0" * (8 - len(bin(n)[2:])) +  bin(n)[2:]
    res = nbin8[:2] + nbin8[-2:]
    res10 = int(res, 2)
    if res10 == 7:
        print(n)