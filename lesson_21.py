import os


# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# #
# # print(p1.__dict__)
# p1.set_coord(2, 4)
# # Point.set_coord(p1)  # применяется редко
#
# p2 = Point()
# p2.set_coord(3, 7)  # изменили значения x и y для данного класса


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone_number = "0-000-000-0000"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print("Персональные данные".center(40, "*"))
#         print(f'Имя: {self.name}\nДень рождения: {self.birthday}\nТелефонный номер: {self.phone_number}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print("=" * 40)
#
#     # def input_info(self):
#     #     self.name = input()
#     #     self.birthday = input()
#     #     self.phone_number = input()
#     #     self.country = input()
#     #     self.city = input()
#     #     self.address = input()
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone_number = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # Получаем имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Johan", "10.06.1992", "89131009999", "RF", "Tomsk", "MIR")
# h1.print_info()
# h1.set_name("John")
# h1.print_info()
# print(h1.get_name())

# Свойства класса могут быть динамические и статические
# class Person:
#     skill = 10  # статическое свойство класса
#
#     def __init__(self, name, surname):  # Инициализатор
#         self.name = name  # динамическое свойство класса
#         self.surname = surname
#         print("Инициализатор Person")
#
#     def __del__(self):  # удаление экземпляра когда он уже не нужен
#         print("Удаление экземпляра класса")
#
#     def print_info(self):
#         print("Данные сотрудника: ", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника: ", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
# # del p1 # удалили ссылку от п1 к классу
# p1 = 5 # сработает также, как и дел, потому что разорвалась ссылка
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)
#
# a = 10
# print(a)
# a = "Hello"
# print(a)

# class Point:
#     count = 0  # у статического св-ва должно быть первоначальное значение в отличае от динамического
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         # self.count += 1#т.к. инициализатор для каждого П работает 1 раз то он будет везде
#         # # 1 кроме поинт.каунт там будет 0
#         Point.count += 1  # тут мы обращаемся к каунт через имя класса
#
#     def get_coord(self):
#         print(self.__dict__)
#
#
# p1 = Point(5, 10)
# p1.get_coord()
# print(p1.count)
# p2 = Point(3, 7)
# p2.get_coord()
# print(p2.count)
# p3 = Point(8, 16)
# p3.get_coord()
# print(p3.count)
#
# print(Point.count)
# print(p1.count)  # так как уже было 3 вызова до этого момента

# культура кода сначала идут __метод__ потом методы с декораторами @ и уже потом простые методы
class Robot:
    count = 0

    def __init__(self, name):
        self.name = name
        print(f'Инициализация робота {self.name}')
        Robot.count += 1

    def __del__(self):
        print(self.name, "выключается!")
        Robot.count -= 1

        if Robot.count == 0:
            print(self.name, "был последним!")
        else:
            print("Работающих роботов осталось", Robot.count)

    def say_hi(self):
        print(f"Приветствую! Меня зовут {self.name}")
        print(f'Численность роботов: {Robot.count}\n')


droid1 = Robot("R2-D2")
droid1.say_hi()
droid2 = Robot("C-3P0")
droid2.say_hi()

print("Роботы могут проделать какую-то работу.\n")

print("Роботы закончили работу давайте их выключим.\n")

del droid1
del droid2

print("Численность роботов", Robot.count)
