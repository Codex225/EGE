for x in range(1, 223000):
    y = (890004 - 4 * x) // 7
    if y >= 2*x + 87000:
        print(x, y)
