from itertools import *

table = 'Выписываем дороги цифрами'
graph = 'Выписываем дороги буквами'

for per in permutations('Выписываем все города буквами'):
    new_graph = table
    for i in range(1, 'Указываем количество городов + 1'):
        new_graph = new_graph.replace(str(i), per[i-1])

    if set(graph.split()) == set(new_graph.split()):
        print('1 2 3 4 5 6')
        print(*per)