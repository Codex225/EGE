def dels(n):
    r = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return r

for n in range(770_000 - 1, 765_000, -1):
    if len(dels(n)) == 0:
        continue
    srzn = int(sum(dels(n)) / len(dels(n)))

    if len(dels(n)) != 0 and  srzn % 100 == 12:
        print(n, srzn)

#единица должна быть в множестве делителей!