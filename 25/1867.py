def dels(n):
    r = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)
    return r

for n in range(500_001, 500_100):
    res = sorted(x for x in dels(n) if x != 8 and x % 10 == 8)
    if len(res) > 0:
        print(n, res[0])