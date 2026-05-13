for n in range(1, 1000):
    nn = int(str(n) + str(n)[-1])
    nnbin = bin(nn)[2:]
    if nnbin.count("1") % 2 == 0:
        nnbin = nnbin + "0"
    else:
        nnbin = nnbin + "1"
    r = int(nnbin, 2)
    if r > 413:
        print(n)
        break
