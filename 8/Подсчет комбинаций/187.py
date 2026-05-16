from itertools import *
c = 0
for m in product("ABCX", repeat=5):
    s = "".join(m)
    if "X" not in s or (s[-1] == "X" and "X" not in s[:-1]):
        c +=1
print(c)