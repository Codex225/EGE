f = open("26_1868.txt")
n = int(f.readline())
data = {}
#По ключу номера ряда сохраняем значения занятых мест
for line in f:
    row, col = [int(x) for x in line.split()]
    #col, row = map(int, line.split())
    if row not in data:
        data[row] = [col] #значение рядов будет списком, и потом добавляем в него новые подходящие
    else:
        data[row].append(col)
#print(data)
ans1 = -1
ans2 = -1
for key in data: #перебираем словарь по ключу
    a = sorted(data[key]) #упорядочиваем список мест в ряду
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] == 3: #проверяем, что места подходящие
            #print(key, a[i]+ 1) # Ответ
            if key > ans1:
                ans1 = key
                ans2 = a[i + 1]
print(ans1, ans2)
#print(data)
