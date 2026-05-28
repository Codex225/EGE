for n in range(7777, 10**9 + 1, 7777):
    x = str(n)[:-2]

    for ch in x:
        if ch in "02468":
            x = x.replace(ch, "c")
        if ch in "13579":
            x = x.replace(ch, "n")

    if x == "cnccncn" and str(n)[-2:] == "77" and len(str(n)) == 9:
        print(n, n // 7777)