from itertools import *
q = 0
for w in product(sorted(set("ПАВСИКАКИЙ")), repeat=6):
    s = "".join(w)
    sp = s
    for x in "АИ": sp = sp.replace(x, "*")
    if "**" in sp or "***" in sp or "****" in sp or "*****" in sp or "******" in sp:
        q += 1
    if s == "КАКААА":
        print(q)
        break