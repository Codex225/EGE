for n in range(100, 1000):
    res = []
    s1 = int(str(n)[0])**2 + int(str(n)[1])**2
    s2 = int(str(n)[1])**2 + int(str(n)[2])**2
    res.append(s1)
    res.append(s2)
    res = sorted(res, reverse=True)


    if "".join(map(str, res)) == "9010":
        print(n)