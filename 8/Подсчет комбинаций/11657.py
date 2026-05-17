from itertools import *
q = 0

for w in permutations("01234567", r=6):
    s = "".join(w)
    if s[0] != "0":
        if "3" not in s:
            for x in "0246": s = s.replace(x, "*")
            if s.count("**") >= 1:
                q += 1
print(q)