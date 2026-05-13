
print("a b c d")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = d and ((a or (not c)) <= (a and b and (not c)))
                if  f:
                    print(a, b, c, d)