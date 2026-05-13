for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n0 = "11" + n2
    else:
        n0 = n2 + "11"
    r = int(n0, 2)
    if r > 102:
        print(n)
        break