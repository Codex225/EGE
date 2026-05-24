class Dog:
    def __init__(self, name):
        self.name = name
        self.k1 = self.k2 = self.k3 = 0

    def voice(self):
        if self.k1 == 2:
            return "Гав"
        self.k1 += 1
        return f"Голос {self.k1}"

    def leg(self):
        if self.k2 == 4:
            return f"Хороший {self.name}"
        self.k2 += 1
        return f"К ноге {self.k2}"

    def sit(self):
        if self.k3 == 3:
            return f"Сидит хороший {self.name}"
        self.k3 += 1
        return f"Сидеть{self.k3}"


dog = Dog('Рекс')
print(dog.voice())
print(dog.voice())
print(dog.leg())
print(dog.sit())
print(dog.sit())
print(dog.voice())
print(dog.sit())
print(dog.sit())
print(dog.voice())

