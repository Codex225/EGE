from itertools import *
q1 = q2 = q = 0
for w in product("ГЕЭ023", repeat=7):
    s = "".join(w)
    q += 1
    if s == "ЕГЭ2023":
        q1 = q
    if s == "2023ЕГЭ":
        q2 = q
        break
print(q2 - q1 - 1)