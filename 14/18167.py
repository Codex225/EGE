for x in range(1, 10000+1):
    d = 6**900 + 6**10 - x
    q3 = q5 = 0
    while d:
        if d % 6 == 3:
            q3 += 1
        if d % 6 == 5:
            q5 += 1
        d //= 6
    if q3 == q5:
        print(x)