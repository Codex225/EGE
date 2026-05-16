from itertools import *
q = 0
for w in permutations("ничья", 5):
    s = "".join(w)
    if s[0] != "ь" and "ьия" not in s:
        q += 1
print(q)