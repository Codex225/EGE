for n in range(128, 256):
    binn = "0"*(8-len(bin(n)[2:])) + bin(n)[2:]
    binn = binn.replace("0", "*")
    binn = binn.replace("1", "0")
    binn = binn.replace("*", "1")

    r = int(binn, 2)
    res = n - r
    if res == 105:
        print(n)