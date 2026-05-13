for n in range(1000, 10000):
    nres = []
    nres.append(int(str(n)[0]) * int(str(n)[1]))
    nres.append(int(str(n)[2]) * int(str(n)[3]))
    nres.sort()
    if "".join(map(str, nres)) == "1214":
        print(n)