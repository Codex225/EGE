from itertools import *
q = 0
for w in permutations("01234567", r=7):
    s = "".join(w)
    if s[0] != "0":
        for x in "0246":
            s = s.replace(x, "0")
        for x in "1357":
            s = s.replace(x, "1")
        if "00" not in s and "11" not in s:
            q += 1
print(q)