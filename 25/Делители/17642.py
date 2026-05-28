def dels(n):
    dels = set()
    for i in range(2, int(n **0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

for n in range(800_001, 800_100):
    rr = dels(n)
    for d in rr:
        if d != 9 and d % 10 == 9:
            print(n, d)
            break
