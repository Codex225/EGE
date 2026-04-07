f = open("26_10726.txt")
n = int(f.readline())
a = [[int(el) for el in l.split()] for l in f]
#print(a)
timeline = [0] * 44641 #это таймлайн, где каждый индекс это квант по минуте. Значение - колво фильмов
for beg, end in a:
    timeline[beg] += 1
    timeline[end] -= 1
print(timeline)
cnt = c = m = s = 0
for t in range(len(timeline)):
    s += timeline[t] #отмечаю изменения
    if s > 0:
        cnt += 1
        c += 1
        m = max(m, c)
    else:
        c = 0
print(cnt, m)
