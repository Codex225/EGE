for n in range(81, 100000):
    binn = bin(n)[2:]
    c0 = binn.count("0")
    c1 = binn.count("1")
    if c0 == c1:
        binn = binn + binn[-1]
    elif c0 < c1:
        binn = binn + "0"
    else:
        binn = binn + "1"
    c0 = binn.count("0")
    c1 = binn.count("1")
    if c0 == c1:
        binn = binn + binn[-1]
    elif c0 < c1:
        binn = binn + "0"
    else:
        binn = binn + "1"
    c0 = binn.count("0")
    c1 = binn.count("1")
    if c0 == c1:
        binn = binn + binn[-1]
    elif c0 < c1:
        binn = binn + "0"
    else:
        binn = binn + "1"
    res = int(binn, 2)
    if res %2 == 0 and res % 4 != 0:
        print(n)
        break