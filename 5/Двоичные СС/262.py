for n in range(1, 128):
    binn = "0"*(8-len(bin(n)[2:])) + bin(n)[2:]
    binn = binn.replace("0", "*")
    binn = binn.replace("1", "0")
    binn = binn.replace("*", "1")
    binn = bin(int(binn, 2) + 1)[2:]
    r = int(binn, 2)
    if r == 221:
        print(n)