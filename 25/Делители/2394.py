

def dels(n):
    dn = set()

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:

            dn.add(i)
            dn.add(n//i)
    return dn

for n in range(670_001, 670_100):
    dns = dels(n)
    dnspr = sum([x for x in dns if len(dels(x)) == 0])
    if dnspr % 10 == 5:
        print(n, dnspr)