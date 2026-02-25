from itertools import product

c = 0
for m in product('лето', repeat=4):
    str = "".join(m)
    if str[0] == "л" or str[0] == "т":
        c += 1
print(c)