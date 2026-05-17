from itertools import *
q = 0
alf = sorted("012345678")
for w in product(alf, repeat=7):
    s = "".join(w)
    if s[0] != "0" and  s[-1] not in "347":
        if "000" not in s and "111" not in s and "222" not in s:
            if "333" not in s and "444" not in s and "555" not in s:
                if "666" not in s and "777" not in s and "888" not in s:
                    q += 1
print(q)


from itertools import *
q = 0
alf = sorted("012345678")
for w in product(alf, repeat=7):
    s = "".join(w)
    if s[0] != "0" and  s[-1] not in "347" and all([d * 3 not in s for d in s]):
        q += 1
print(q)