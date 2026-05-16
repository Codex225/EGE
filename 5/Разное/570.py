resm = -10000000
for n in range(1, 256):
    binn = (8 - len(bin(n)[2:])) * "0" + bin(n)[2:]
    binn_rev = binn[::-1]
    #print(binn, binn_rev)
    res = int(binn,2) - int(binn_rev,2)
    resm = max(resm, res)

print(resm)

