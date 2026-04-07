f = open("26_10726.txt")
n = int(f.readline())
a = [[int(el) for el in l.split()] for l in f]
#print(a)
timline = [0] * 44641 #это таймлайн, где каждый индекс это квант по минуте. Значение - колво фильмов
for beg, end in a:
    for t in range(beg,end):
        timline[t] += 1
print(timline)
s = c = m = 0
for t in range(len(timline)):
    if timline[t] > 0: #идет хоть один фильм
        s += 1
        c += 1
        m = max(m, c)
    else:
        c = 0

print(s, m)
