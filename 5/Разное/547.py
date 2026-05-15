for n in range(1, 1000):
    binn = bin(n)[2:]
    if binn.count('1') % 2 == 0:
        binn = binn + "0"
    else:
        binn = binn + "1"
    if binn.count('1') % 2 == 0:
        binn = binn + "0"
    else:
        binn = binn + "1"
    if int(binn, 2) > 103:
        print(n)
        break