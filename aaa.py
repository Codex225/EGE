
class ShoppingList:
    def __init__(self, *args):
       self.shop = list(args)

    def values(self):
        return self.shop

    def append(self, value):
        self.shop.append((value, False))

    def check(self, value):
        for i in range(len(self.shop)):
            if self.shop[i][0] == value:
                self.shop[i] = (self.shop[i][0], True)

    def checked_values(self):
        return [x for x in self.shop if x[1]]

    def rest_values(self):
        return [x for x in self.shop if not x[1]]


class TODOList:
    def __init__(self, *args):
        self.shop = sorted(args, key=lambda x: -x[1])

    def values(self):
        return self.shop

    def append(self, value, urgency):
        self.shop.append((value, urgency, False))
        self.shop = sorted(self.shop, key=lambda x: -x[1])

    def check(self, value):
        for i in range(len(self.shop)):
            if self.shop[i][0] == value:
                self.shop[i] = (self.shop[i][0], self.shop[i][1], True)

    def checked_values(self):
        return [x for x in self.shop if x[2]]

    def rest_values(self):
        return [x for x in self.shop if not x[2]]


class Route:
    def __init__(self, *args):
        self.stops = list(args)

    def values(self):
        return self.stops

    def append(self, value, time):
        if self.stops:
            prev = self.stops[-1][1].split(":")
            prev = int(prev[0]) * 60 + int(prev[1])
            present = time.split(":")
            present = int(present[0]) * 60 + int(present[1])
            if present > prev:
                self.stops.append((value, present, False))
        else:
            self.stops.append((value, time, False))

    def check(self, value):
        for i in range(len(self.stops)):
            if self.stops[i][0] == value:
                self.stops[i] = (self.stops[i][0], self.stops[i][1], True)

    def checked_values(self):
        return [x for x in self.stops if x[-1]]

    def rest_values(self):
        return [x for x in self.stops if not x[-1]]

path = Route(("Stratford", "12:15", False),
             ("Hackney Central", "12:24", False),
             ("Dalston Kingsland", "12:36", False))
path.append("Camden Road", "12:45")
path.append("Richmond", "11:52")
print(*path.values(), sep="\n")
print()
path.check("Stratford")
path.check("Hackney Central")
print(*[x[0] for x in path.rest_values()], sep="\n")


# td = TODOList(("buy car", 5, False),
#               ("make lessons", 1, False),
#               ("wright poem", 4, False))
# td.append("wash pet", 4)
# td.check("buy car")
# print(*td.checked_values(), sep="\n")
# print()
# print(*td.values(), sep="\n")
#






# shop = ShoppingList(("potato", False),
#                     ("milk", False),
#                     ("bread", False))
# shop.append("apple")
# shop.check("bread")
# print(*shop.values(), sep="\n")
# shop.check("milk")
# print()
# print(*[x[0] for x in shop.checked_values()],
#       sep="\n")
# print()
# print(*[x[0] for x in shop.rest_values()],
#       sep="\n")
# import random
#
# def random_mark():
#     mark = random.randint(1, 5)
#     marks = {
#         5: 'Так держать!🔥',
#         4: 'В следующий раз получится лучше.🙂',
#         3: 'Надо ещё постараться.😕',
#         2: 'Не прошло.😞',
#         1: 'Нет слов.',
#     }
#     return f'Оценка {mark}: {marks[mark]}'
#
# print(random_mark())

# from PIL import Image
#
# im = Image.open("roses.png")
# w, h = im.size
# im_new = Image.new("RGB", (2 * w, h))
# im_new.paste(im, (0, 0))
# im2 = im.transpose(Image.FLIP_LEFT_RIGHT)
# im_new.paste(im2, (w, 0))
# im_new.save("mirror.png")


# from PIL import Image
#
# im = Image.open("image.png")
# size = im.size
# x, y, w, h = [int(x) for x in input().split()]
# x0, y0 = max(0, x), max(0, y)
# x, y = min(x0 + w, size[0]), min(y0 + h, size[1])
# im = im.crop((x0, y0, x, y))
# im.save("part.png")