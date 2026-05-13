for x in range(67):
    d = 3*81**3 + x*81**2 + 2 * 81 ** 1 + 1 + 1*67**3 + 7 * 67**2 + x *67**1 + 4
    if  d % 35 == 0:
        print(x, d // 35)

# def f(x, base):
#     a = x[::-1]
#     sm = 0
#     for t in range(len(a)):
#         sm += a[t] * base ** t
#     return sm
#
# for x in range(67):
#     v = f([3, x, 2, 1], 81) + f([1, 7, x, 4], 67)
#     print(v)