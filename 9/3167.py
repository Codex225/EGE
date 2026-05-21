f = open("9_3167.txt")
q = 0
for line in f:

    rl = [int(x) for x in line.split()]

    if (max(rl) + min(rl))**2 > sorted(rl)[1]**2 + sorted(rl)[2]**2:
        q += 1
print(q)