from itertools import product
c = 0
alf = sorted("ШКОЛА")
for s in product(alf, repeat=5):
    s = "".join(s)
    c += 1
    if s == "ШАЛАШ":
        print(s, c)
print(c)