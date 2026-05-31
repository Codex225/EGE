class Pencil:
    def write(self, line):
        return line.lower()

class Pen:
    def write(self, line):
        return line.title()

class Marker:
    def write(self, line):
        return line.upper()

pencil = Pencil()
print(pencil.write('Тема сегодняшнего урока: Полиморфизм'))
pen = Pen()
print(pen.write('Тема сегодняшнего урока: Полиморфизм'))
marker = Marker()
print(marker.write('Тема сегодняшнего урока: Полиморфизм'))