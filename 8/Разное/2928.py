from itertools import *
q = 0
for w in product("0123456", repeat=7):
    s = "".join(w)
    if s[0] not in "035":


        if (s.count("22") == 0 and s.count("44") >= 1) or (s.count("22") >= 1 and s.count("44") == 0)\
                or (s.count("22") == 0 and s.count("44") == 0):
            q += 1
print(q)

# from itertools import *  # импортируем все нужные функции из itertools для перебора вариантов
# k = 0  # заводим счётчик подходящих чисел
# for x in product('0123456', repeat=7):  # перебираем все 7-значные записи в семеричной системе
#     s = ''.join(x)  # собираем строку числа из кортежа цифр
#     if s[0] != '0' and s[0] != '3' and s[0] != '5' and not ('22' in s and '44' in s):  # проверяем запрет первых цифр и одновременное наличие 22 и 44
#         k += 1  # увеличиваем счётчик, если число подходит
# print(k)  # выводим количество подходящих чисел