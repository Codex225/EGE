from itertools import *
q = 0
for w in product(sorted("УДАЧ"), repeat=5):
    s = "".join(w)

    if s[0] in "УА":
        q += 1
        if s == "УДАЧА":
            print(q)
            break