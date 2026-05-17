from itertools import *
q = 0
for w in product(sorted("ФЕВРАЛЬ"), repeat=6):
    s = "".join(w)
    q += 1
    if all([x not in "ЕА" for x in s]):
        print(s, q)
        break