for n in range(1, 10000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n0 = n2 + "01"
    else:
        n0 = n2 + "10"
    r = int(n0, 2)
    if r > 81:
        print(r)
        break