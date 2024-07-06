import os

# Инкапсуляция - защита данных от доступа из вне (сокрытие)
# модификаторы доступа:
# public - self.name - открытый доступ
# protected - self._name - используется при наследовании
# private - self.__name - защищенная переменная для доступа из вне

# class Point:
#     def __init__(self, x, y):
#         # self.__x = x  # private
#         # self.__y = y  # private
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y

#
#     def __check_value(s):  # функция для проверки заменяет строку ив в set_coord и эта ф-ия(метод) приватна также
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установка новых значений и условий СЕТ - Сеттер
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("coords need number")
#
#     def get_coord(self):  # получаем значения
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# print(p1._Point__x, p1._Point__y)
# # p1.set_coord(100, "abc")
# p1.set_coord(100, 500.5)
# print(p1.__dict__)
# print(p1.get_coord())
# # print(p1.__x, p1.__y)
# # print(p1.x, p1.y)
# # p1.x = 100
# # p1.y = "abc"
# # print(p1.x, p1.y)  # невозможные координаты так как буквы
import math


class Rectangle:  # где-то ошибка проверить и сравнить с тем что ниже
    def __init__(self, length, width):
        self.__length = length
        self.__width = width


    def __check_value(s):  # в дикс будет _Rectangle__check_value
        if isinstance(s, int) or isinstance(s, float):
            return True
        return False

    def set_width(self, value):
        if Rectangle.__check_value(value):
            self.__width = value

    def set_length(self, value):
        if Rectangle.__check_value(value):
            self.__length = value

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def get_area(self):
        return self.__length * self.__width

    def get_perimetr(self):
        return 2 * (self.__length + self.__width)

    def get_hypotinuse(self):
        return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)

    def draw(self):
        print(("*" * self.__width + "\n")7 * self.__length)


a = Rectangle(4, 12)
a.set_length(3)
a.set_width(9)
print("Длинна прямоугольника:", a.get_length())
print("Ширина прямоугольника:", a.get_width())
print("Периметр прямоугольника:", a.get_perimetr())
print("Гипотенуза прямоугольника:", a.get_hypotinuse())
a.draw()
#досмотреть с час 30
#__slots__ = [] - в список добавляют разрешенные переменные, те которых там нет не будут работать в классе
    # не позволяет создавать переменные которы нет в списке даже через инит
# с слотс дикт не работает и выдает ошибку
    # __set_x(self,x) и __get_x(self,x) - приватные методы присвоения внутри как инит на 1 переменную
    # истобы изменить переменную надо ввести метот  x = property(__get_x,__set_x) и теперь можно через p1.x получить доступ
    #
