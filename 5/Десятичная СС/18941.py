for n in range(1000, 10000):
    res = []
    s = [int(x) for x in str(n)]
    #print(s)
    res.append(s[0] * s[1])
    res.append(s[0] * s[2])
    res.append(s[0] * s[3])
    res.sort()
    if str(res[1]) + str(res[2]) == "5472":
        print(n)