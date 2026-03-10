from math import *
f = open("27_A_21425.txt")
data = []
for line in f:
    x, y = [float(el) for el in line.replace(",", ".").split()]
    data.append([x, y])
    #print(data)
clusters = []
eps = 3
while data: #перебираем точки, пока они есть в сырых данных, т.е. пока они не изучены
    cluster = [data.pop()] #собираем кластер на основе точки
    for p1 in cluster: # перебираем все точки из текущего кластера
        neib = [p2 for p2 in data if dist(p1, p2) < eps] #собираем список соседей для текущей точки
        cluster.extend(neib) #получившихся соседей добавляю в этот кластер
        for p in neib: #удаляем "изученные" точки
            data.remove(p)
    clusters.append(cluster) #после сбора кластера добавляю его в список всех кластеров

print(len(clusters), [len(cl) for cl in clusters])
