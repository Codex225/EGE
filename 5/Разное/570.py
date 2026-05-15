maxn = -1000000
for n in range(1, 256):
    binn = (8 - len(bin(n)[2:]))*'0' + bin(n)[2:]
    binnrev = bin(n)[2:][::-1]
    res = int(binn, 2) - int(binnrev,2)
    #print(res)
    maxn = max(maxn, res)
print(maxn)