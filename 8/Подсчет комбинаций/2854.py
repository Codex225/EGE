from itertools import *

q = 0
for w in set(permutations("росомаха", 8)):
    s = "".join(w)
    for sg in "рсмх": s = s.replace(sg, "1")
    for gl in "оа": s = s.replace(gl, "0")
    if "00" not in s and "11" not in s:
        q += 1
print(q)
