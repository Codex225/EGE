print("x y z f")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = ((not x) and (not z)) or (x and y)
            if f:
                print(x, y, z, int(f))