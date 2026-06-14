class Platypus:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f"Меня зовут {self.name}"

    def make_sound(self):
        return f"{self.name} издаёт звук: Кря-кря!"


class BabyPlatypus(Platypus):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def get_weight(self):
        return f"Мой вес: {self.weight} грамм"

    def make_sound(self):
        return f"{self.name} пищит: Пи-пи!"


adult = Platypus("Перри")
print(adult.make_sound())
baby = BabyPlatypus("Малыш", 500)
print(baby.make_sound())