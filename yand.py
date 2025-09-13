def borders(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    if x3 < x1 and x3 > x2 and y3 < y1 and y3 > y2:
        return print("INSIDE")
    elif x3 >= x1 and x3 <= x2 and y3 == y1:
        return print("AT THE EDGE")
    elif x3 >= x1 and x3 <= x2 and y3 == y2:
        return print("AT THE EDGE")
    elif (y3 > y2) and (y3 < y1) and x3 == x1:
        return print("AT THE EDGE")
    elif (y3 > y2) and (y3 < y1) and x3 == x1:
        return print("AT THE EDGE")
    else:
        return print("OUTSIDE")


borders((1, 3), (4, 0), (2, 2))
