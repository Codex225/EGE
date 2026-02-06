# (№ 3018) Текстовый файл содержит строку из заглавных латинских букв,
# всего не более чем из 106 символов. Определите количество подстрок
# длиной не менее 17 символов, которые начинаются и заканчиваются буквой A
# и не содержат других букв A (кроме первой и последней) и букв B.
from pprint import pprint

f = open("24_3018.txt")
s = f.readline().strip()
# pprint(s)
q = 0
for i in range(len(s) - 17):
    for j in range(i +17, i):
        res = s[i: j+1]
        if res[0] == "A" and res[-1] == "A" and ("A" not in res[1:-1]) and "B" not in res:
            q += 1
print(q)
