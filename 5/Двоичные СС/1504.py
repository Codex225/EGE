for n in range(1, 10000):
    binn = bin(n)[2:]
    binn = binn.replace("0", "00").replace("1", "11")
    r = int(binn, 2)
    if r > 63:
        print(r)
        break