lmin = 10 ** 100
for i in range(3):
    l = input()
    if len(l) < lmin:
        lmin = len(l)
print(lmin)
