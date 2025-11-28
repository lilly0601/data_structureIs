class Figure:
    def __init__(self, color="кара"):
        self.color = color  

    def change_color(self, new_color):
        """Фигураның түсін өзгерту әдісі"""
        self.color = new_color

    def info(self):
        return f"Бұл {self.color} түсті фигура."


class Oval(Figure):
    def __init__(self, radius1, radius2, color="Кара"):
        super().__init__(color)
        self.radius1 = radius1
        self.radius2 = radius2

    def info(self):
        return f"{self.color} түсті сопақ. Радиустары: {self.radius1}, {self.radius2}"


class Square(Figure):
    def __init__(self, side, color="Кара"):
        super().__init__(color)
        self.side = side

    def info(self):
        return f"{self.color} түсті шаршы. Қыры: {self.side}"


r1 = int(input("Сопақтың бірінші радиусын енгізіңіз: "))
r2 = int(input("Сопақтың екінші радиусын енгізіңіз: "))
color_oval = input("Сопақтың түсін енгізіңіз: ")
oval = Oval(r1, r2, color_oval)

side = int(input("Шаршының қырын енгізіңіз: "))
color_square = input("Шаршының түсін енгізіңіз: ")
square = Square(side, color_square)

print("\nФигуралар туралы ақпарат:")
print(oval.info())
print(square.info())

new_color = input("\nШаршыға жаңа түс енгізіңіз: ")
square.change_color(new_color)
print("Түсті өзгерткеннен кейін:", square.info())
