f = open("27_A_18314.txt")
#после анализа данных x = 24  разделяет кластеры
#заменяем запятые на точки
clusters = [[], []] #здесь будут все координаты наших точек
for s in f:
    x, y = [float(i) for i in s.split()]
    if x > 24:
        clusters[1].append([x, y])
    else:
        clusters[0].append([x, y])
#print(clusters)
#точки разбили по кластерам

def r(p1, p2): #манхэттенское расстояние
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def center(cl):
    l = []
    for p1 in cl: #возможный центр этого кластера
        sm = 0 # сумма расстояний от этой точки до остальных
        for p2 in cl:
            sm += r(p1, p2) # r -это то самое манхэттенское расстояние из задачи
        l.append([sm,p1]) #после того как общая сумма посчитается, а также координаты точки p1
    return min(l)[1] #Возвращаем координаты самой точки

centers = [center(i) for i in clusters]

print(centers)
#теперь можно руками, визуально проверить, что все правильно
# px = (centers[0][0] + centers[1][0]) / 2
# py = (centers[0][1]+ centers[1][1] ) /2

px = sum([t[0] for t in centers])/ len(centers)
py = sum([t[1] for t in centers])/ len(centers)
print(int(abs(px *1000)), int(abs(py *1000)))

# def line (x1, y1, x2, y2):
#     k = (y2 - y1) / (x2 - x1)
#     b = y2 - k * x2
#     return [k, b]
#
#23509 554




