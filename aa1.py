class Pigtail():
    def __init__(self, line):
        self.line = line

    def one_strip(self):
        pig = ""
        x = len(self.line)//2
        for i in range(x):
            if i %4 ==0:
                pig += "  " + self.line[x - i - 1] + self.line[x + 1] + "  "
            elif i % 2 == 1:
                pig += " " + self.line[x - i - 1] +  "  " + self.line[x + i] + " "
            else:
                pig += self.line[x - i - 1] + "    " + self.line[x + i]
            if i != x - 1:
                pig += "\n"
        return pig


pigtail = Pigtail('ABCDEFGHIJKLMNOPQRSTUVWX')
print("Одинарная косичка:")
print(pigtail.one_strip())