def dels(n):
    res = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res.add(i)
            res.add(n//i)
    return res

for n in range(452_022, 453_021):
    if len(dels(n)) == 0:
        m = 0
    else:
        m = max(dels(n)) + min(dels(n))
    if m % 7 == 3:
        print(n, m)