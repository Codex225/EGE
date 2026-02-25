for a in range(1, 100000):
    flag = True
    for x in range(1, 40000):
        for y in range(1, 40000):

            f = (3 *x + 4 * y) or (y < x - 1222) or (y > a)
            if f == 0:
                flag = False
                break
    if flag: print(a)
