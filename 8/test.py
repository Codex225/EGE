from itertools import permutations as per, product as p

c = 0
s = "ворота"
k = set(s)
print(k)
for i in per(k, 5):
    str = "".join(i)
    print(str)
    if "оа" not in str and "оо" not in str and "ао" not in str:
        c +=1
print(c)