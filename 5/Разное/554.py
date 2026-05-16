q = 0
s = set()
for n in range(1, 100000):
    binn = bin(n)[2:]
    binn = binn + str(binn.count('1') % 2)
    binn = binn + str(binn.count('1') % 2)
    r = int(binn, 2)
    if 20 <= r <= 50:
        s.add(r)
print(len(s))
