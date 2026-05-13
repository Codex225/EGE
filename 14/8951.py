for n in range(6, 1000):
    d = 7**500 - 5*n - 3
    if d % 6 == 0:
        print(n)
        break