from itertools import product


# Часть 1: Вычисление L
def calculate_L():
    # Сначала выбираем 2 места для цифры 4
    combinations_for_4 = 66  # C(12, 2)

    # Для оставшихся 10 позиций можем поставить 3 возможные цифры (1, 2 или 3)
    possibilities_for_other_digits = 3 ** 10

    # Количество чисел, где цифра 4 используется ровно дважды
    L = combinations_for_4 * possibilities_for_other_digits
    return L


# Часть 2: Вычисление M
def calculate_M():
    count = 0

    # Перебираем все возможные 10 цифр, которые могут быть в числе (цифры 1, 2 или 3)
    for digits in product([1, 2, 3], repeat=10):
        sum_digits = 4 * 2 + sum(digits)  # Сумма цифр (две цифры 4 и сумма оставшихся цифр)

        if sum_digits % 9 == 0:
            count += 1

    # Количество таких чисел
    M = count * 66  # Умножаем на количество способов выбрать два места для цифры 4
    return M


# Вычисления
L = calculate_L()
M = calculate_M()

print(L, M)
