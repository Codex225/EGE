from itertools import product

cnt = 0
for ln in range(3, 8):
    for w in product("КСЕНИЯ", repeat=ln):
        s = "".join(w)
        s = s.replace("К", "Н").replace("С", "Н")
        if s.count("Е") <= 2 and s.count("И") <= 2 and s.count("Я") <= 2:
            if (s[0] == "Н" and s.count("Н") == 1) or not "Н" in s:
                cnt += 1
print(cnt)