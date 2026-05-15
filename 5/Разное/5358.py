for n in range(6, 1000):
    binn = bin(n)[2:]
    lbinn = [int(x) for x in binn]
    if binn[:3].count("1") % 2 == 0:
        binn = "1" + binn[:-2] + "01"
    else:
        binn ="10" + binn[2:] + "1"
    r = int(binn, 2)
    if r > 50:
        print(n)
        break