for x in range(1, 1000):
    x2 = bin(x)[2:]
    x2 = x2 + str(x2.count("1") % 2)
    x2 = x2 + str(x2.count("1") % 2)
    res = int(x2, 2)
    if res > 80:
        print(res)
