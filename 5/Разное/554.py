q = 0
s = set()
for n in range(20, 51):
    binn = bin(n)[2:]
    binn = binn + str(binn.count('1') % 2)
    binn = binn + str(binn.count('1') % 2)
    r = int(binn, 2)
    s.add(r)
print(s)
