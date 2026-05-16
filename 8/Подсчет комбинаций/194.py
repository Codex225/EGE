from itertools import product
q = 0
for w in product("катер", repeat=3):
    s = "".join(w)
    if s.count("р") >= 2:
        q +=1
print(q)