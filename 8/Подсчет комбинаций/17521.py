from itertools import *
alf = "01234567"
q = 0
for w in product(alf, repeat=5):
    s = "".join(w)
    if s[0] != "0" and s[0] not in "1357" and s[-1] not in "26" and s.count("7") <= 2:
        q +=1
print(q)