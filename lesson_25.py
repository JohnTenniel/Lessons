# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         self.__width = width
#         self.__height = height
#         super().__init__(color)
#
#     def area(self):
#         if not isinstance(self.__width, int) or not isinstance(self.__height,
#                                                                int) or self.__width < 0 or self.__height < 0:
#             raise TypeError("Ширина и высота должны быть числом больше нуля")
#         else:
#             print(f"Прямоугольник {self.color}, Площадь:", end="")
#             return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.area())

# Наследование от встроенных типов

# class Vector(list):  # [1, 2, 3] = > 1 2 3
#     def __str__(self):
#         return " ".join(map(str, self))  # self - обращение к переменной в лист
#
#
# v = Vector([1, 2, 3])
# v.append(4)
# print(v)
# print(type(v))

# перегрузка методов - послушать описание заново

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"x = {self.x}, y = {self.y}"
#
#     def set_coord(self, x=None, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(10, 20)
# print(p1)
# p1.set_coord(1, 3)
# print(p1)
# p1.set_coord(5)
# print(p1)
# p1.set_coord(y=7)
# print(p1)

# абстрактный метод

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self.width = width
            self.length = length
        else:
            self.radius = radius

    def calc_area(self):
        raise NotImplementedError("В дочернем классе должен быть реализован метод area()")


class SqTable(Table):  # наследование от класса Table
    def calc_area(self):
        return self.width * self.length


class RoundTable(Table):
    def calc_area(self):
        return round(pi * self.radius ** 2, 2)


t = SqTable(20, 10)
print(t.__dict__)
print(t.calc_area())
t2 = RoundTable(radius=20)
print(t2.__dict__)
print(t2.calc_area())

# Досмотреть после перерыва
