def f(n):
    res = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(i)
            res.append(i)

    return res

# dels =[]
# for n in range(174457, 174505 + 1):
#     if f(n) == 2:
#         print(f(n))

print(f(6))

