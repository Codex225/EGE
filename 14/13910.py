for p in range(2, 37):
    if (ord("t") - 87) * p + (ord("h") - 87) + (ord("n") - 87) * p + ord("q") - 87 + ord("u") - 87 == p**2 + (ord("l") - 87) * p + 7:
            print(p)