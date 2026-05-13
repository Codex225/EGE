for n in range(1, 10000):
    n = n - n % 4
    binn = bin(n)[2:]
    if binn.count("1") % 2 == 0:
        binn = binn + "0"
    else:
        binn = binn + "1"
    if binn.count("1") % 2 == 0:
        binn = binn + "0"
    else:
        binn = binn + "1"
    r = int(binn, 2)
    if r >100:
        print(r)
        break