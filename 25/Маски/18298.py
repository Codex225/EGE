from fnmatch import fnmatch

for n in range(1996, 10**10, 1996):
    x = str(n)
    if fnmatch(x, "1592*6?8") and all(k in "02468" for k in x[4:-3]):
        print(n, n // 1996)

#all для пустого списка вернет всегда True!, поэтому вариант нулевого среза обрабатывать спецом
#не надо.