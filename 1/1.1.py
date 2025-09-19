
from itertools import permutations

table = "14 15 17 23 25 28 32 34 35 38 41 43 46 47 51 52 53 64 67 68 71 74 76 82 83 86"
graph = "аб аг ае ба бд бв вб вд ви га гд гж ге дг дб дв ди еа ег еж же жг жи иж ид ив"

for per in permutations("абвгдежи"):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(graph.split()) == set(new_graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)