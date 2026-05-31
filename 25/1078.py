def dels(n):
    r = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)


    return r

# for n in range(1204300, 1204380 + 1):
#     #print(len([x for x in dels(n) if x % 2 != 0]))
#     if sum(dels(n)) != 0 and   sum(dels(n)) % 10 == 0:
#         print(n, sum(dels(n)), dels(n))
#         break

for n in range(1204300, 1204381):
    d = [i for i in dels(n) if i % 2==0]
    s = sum(d)
    if s!= 0 and s%10 == 0:
        print(n, s)