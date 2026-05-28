def dels(n):
    dn = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            dn.add(i)
            dn.add(n//i)
    if len(dn) == 0:
        return 0
    else:
        return int(sum(dn)/len(dn))

for n in range(550_001, 550_100):
    rr = dels(n)
    if rr and rr % 31 == 13:
        print(n, rr)