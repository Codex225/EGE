for x in range(1, 1000):
    binn = bin(x)[2:]
    if x % 2 == 0:
        binn = "1" + binn + "0"
    else:
        binn = "11" + binn + "11"
    r = int(binn, 2)
    if r > 52:
        print(r)