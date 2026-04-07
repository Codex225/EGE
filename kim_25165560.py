


#8
# from itertools import product
# alf = "0123456789abc"
# q = 0
# s = product(alf, repeat=5)

# for i in s:
#     #print("".join(list(i)))
#     str = "".join(i)
#
#
#     if str[0] != "0" and "a" not in str and len(set(str)) == 5:
#         str = str.replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1").replace("b", "1")
#         str = str.replace("2", "0").replace("4", "0").replace("6", "0").replace("8", "0").replace("a", "0").replace("c", "0")
#         if "11" not in str and "00" not in str:
#             print(str)
#             q += 1
# print(q)





# #7
# k = 4
# t = 2 * 60 * 60
# nu = 192 * 1000
# i = 16
# I = k * t * nu * i
# print(I)
#
# vp = 38400 * 5 * 60 * 60
# print(I / vp)

##6
# from turtle import *
# tracer(0)
# m = 30
# lt(90)
# screensize(5000, 5000)
# for i in range(2):
#     fd(m * 11); lt(270); bk(m * 11); rt(90)
# penup()
# fd(m * 5); rt(90); bk(3 * m); lt(90)
# pendown()
# for i in range(2):
#     fd(m * 8); rt(90); fd(m * 12); rt(90)
# penup()
# fd(3 * m); rt(180); bk(6 * m)
# pendown()
# for i in range(2):
#     fd(m * 9); rt(90); fd(m * 7); rt(90)
# penup()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(3, "red")
#
# update()
# done()

# #5
# res = []
# for n in range(1, 10000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = n2 + "0"
#     else:
#         n2 = n2 + "1"
#     if n2.count("0") % 3 == 0:
#         n2 = "11" + n2[2:]
#     else:
#         n2 = "10" + n2[2:]
#
#     #print(n2)
#     r = int(n2, 2)
#
#     if r < 400: res.append(r)
# print(max(res))