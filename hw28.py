import math


class Shape:
    def __init__(self, color):
        self.color = color

    def get_perimeter(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод get_perimeter()")

    def get_area(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод get_area()")

    def draw(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод draw()")

    def info(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод info()")


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        super().__init__(color)

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side * self.side

    def draw(self):
        return ("*  " * self.side + "\n") * self.side

    def info(self):
        print(f"=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.get_area()}"
              f"\nПериметр: {self.get_perimeter()}\n{self.draw()}")


class Rectangle(Shape):
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        super().__init__(color)

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width

    def draw(self):
        return ("*  " * self.width + "\n") * self.length

    def info(self):
        print(f"=== Прямоугольник ===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}\n"
              f"Площадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}")


class Triangle(Shape):
    def __init__(self, side_x, side_y, side_z, color):
        self.side_x = side_x
        self.side_y = side_y
        self.side_z = side_z
        super().__init__(color)

    def get_perimeter(self):
        return (self.side_x + self.side_y + self.side_z) / 2

    def get_area(self):
        p = self.get_perimeter()
        return round(math.sqrt(p * (p - self.side_x) * (p - self.side_y) * (p - self.side_z)), 2)

    def draw(self):
        row = []
        for n in range(self.side_y):
            row.append("   " * n + "*  " * (self.side_x - 2 * n) + "   " * n)
        return "\n".join(sorted(row))

    def info(self):
        print(f"=== Треугольник ===\nСторона 1: {self.side_x}\nСторона 2: {self.side_y}\nСторона 3: "
              f"{self.side_z}\nЦвет: {self.color}\nПлощадь: {self.get_area()}\n"
              f"Периметр: {self.get_perimeter()}\n{self.draw()}")


figs = [Square(3, "red"), Rectangle(3, 7, "green"), Triangle(11, 6, 6, "yellow")]

for g in figs:
    g.info()
