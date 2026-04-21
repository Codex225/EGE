s = map(float, input().split())
data = dict.fromkeys(["до 10", "от 10 до 100", "от 100 до 1000", "свыше 1000"])
for key in data.keys():
    data[key] = []
#print(data)
for value in s:
    if value < 10:
        print("VALUE", value)
        data["до 10"].append(value)
    elif value < 100:
        data["от 10 до 100"].append(value)
    elif value < 1000:
        data["от 100 до 1000"].append(value)
    else:
        data["свыше 1000"].append(value)
#print(data)
for key in data:
    n = len(data[key])
    if n:
        avg = sum(data[key]) / n
        print(f"{key}: {n}, {avg:.1f}")












# a = [1, 2, 3]
# b = [4, 5, 6]
# a = a + b
# c = [7, 8, 9]
#
# print(a)
#
#
#
#
#
#
#
#
#
#
#







# numbers = [int(x) for x in input().split()]
# res = []
#
# for number in numbers:
#     temp = {"digits": 0, "units": 0, "zeros": 0}
#     while number:
#         d = number % 2
#         if d:
#             temp["units"] += 1
#         else:
#             temp["zeros"] += 1
#         temp["digits"] += 1
#         number //= 2
#     res.append(temp)
# print(res)