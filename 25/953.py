def dels(n):
    r = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)
    return r

for n in range(500_000, 499_000, -1):
    res = dels(n)
    #print(res)

    ress = [x for x in res if len(dels(x)) == 0]
#    print(ress)
    if sum(res) > 0 and sum(ress) != 0 and sum(ress) % 10 == 0:
        print(n, sum(ress))
