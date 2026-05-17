from itertools import *
q = 0
for w in product("ГЕКЭ023", repeat=4):
    s = "".join(w)
    q += 1
    if s[0] in "023" and (not any([x*2 in s for x in s])):
        print(s, q)