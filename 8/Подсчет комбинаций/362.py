from itertools import *
q = 0
for w in product("джобс", repeat=6):
    s = "".join(w)
    if s.count("д") == s.count("о") == s.count("с") == 1 and s.count("ж") <= 2:
        q += 1
print(q)