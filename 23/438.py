def f(x, y):
    if x > y: return 0
    elif x == y: return 1
    s = str(x)  # Преобразуем число в строку для работы с разрядами
    a, b = int(s[0]), int(s[1])  # Для двухзначных: a — старший разряд, b — младший разряд
    t = 0
    if x % 10 != 0:
        t += f(x + b, y)
    if x >= 20:
        t += f(x * a, y)
    if a != b:
        t += f(x + abs(a-b), y)
    return t

print(f(21, 62))