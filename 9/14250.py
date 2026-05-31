q = 0
summ = 0
for r in open("9_14250.txt"):
    res = [int(x) for x in r.split()]
    q += 1
    if len(set(res)) == 6 and (max(res) - min(res))**3 >= (sum(res) - max(res) - min(res)) ** 2:
        summ += q
print(summ)

