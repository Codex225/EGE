#
# res = []
# for x in range(1, 11501):
#     #nn = 7**270 + 7**170 + 7**70 - x
#     nn = 1000 - x
#     n = nn
#     q0 = mq0 = 0
#     while n:
#         if n % 7:
#             q0 += 1
#         n = n//7
#     if q0 == 4:
#         print(nn, x)

def f7(x):
    res = []
    s = ""
    while x:
        res.append(x % 7)
        s = s + str(x % 7)
        x = x // 7
    return res[::-1], s[::-1], res.count(0), s.count('0')
m0 = 0
for x in range(1, 11501):
    n = 7**270 + 7 **170 + 7**70 - x
    m0 = max(m0, f7(n)[2])
    if f7(n)[2] == 203:
        print(x)
print(m0)