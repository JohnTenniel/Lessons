# class String:
#     def __init__(self, value):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
class ValidString:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        # print(instance)
        if not isinstance(value, str):
            raise ValueError(f"{self.__name} должно быть строкой")
        instance.__dict__[self.__name] = value

class Person:
    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     if not isinstance(value, str):
    #         raise TypeError("Error")
    #     self.__name = value
    #
    # @property
    # def surname(self):
    #     return self.__surname
    #
    # @name.setter
    # def surname(self, value):
    #     if not isinstance(value, str):
    #         raise TypeError("Error")
    #     self.__surname = value


p = Person(12, "ivan")
# посмотреть начало


# Создание модулей
# import math
# import random
# from geometry import rect, sq, trian
# # import geometry.rect
# # import geometry.sq
# # import geometry.trian
# # from geometry import *
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimeter())
#
# if __name__ == "__main__":
#     run()

# # from Car import electrocar
# from Car.electrocar import ElectroCar
#
# # e_car = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
# e_car = ElectroCar("Tesla", "T", 2018, 99000)
# e_car.show_car()
# e_car.description_battery()
#
# # пересмотерть последний час про Json и pip
