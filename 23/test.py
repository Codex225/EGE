def f(start, end, p1, p2):
    if start == 30:
        p1 = 1
    if start == 60:
        p2 = 1
    if start > end or (start > 60 and p1 == p2):
        return 0
    if start == end:
        return 1


    return f(start + 1, end, p1, p2) + f(start * 2, end, p1, p2) + f(start * 3, end, p1, p2)

print(f(10, 70, 0, 0))