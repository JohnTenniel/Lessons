class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if not isinstance(n, str):
            raise TypeError("Имя должно быть строкой")
        else:
            self.__name = n

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, o):
        if not isinstance(o, int):
            raise TypeError("Возраст должен быть целым числом")
        else:
            self.__old = o

    @old.deleter
    def old(self):
        del self.__old


# не понял почему 26 в задании в возрасте если перед этим мы изменяем значение на 31
# но сделал как на картинке
p1 = Person("Irina", 26)
print(p1.__dict__)
p1.name = "Igor"
p1.old = 31
print(p1.name)
print(p1.old)
del p1.name
p1.old = 26
print(p1.__dict__)
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# print(p1.name)
# print(p1.old)
# del p1.name
# print(p1.__dict__)
# print()
# print()
# p1.name = "Arkadiy"
# p1.old = 36
# print(p1.__dict__)
# print(p1.name)
# print(p1.old)
# print(p1.name)
# del p1.name
# # print(p1.name) #проверка на удаление имени
# print(p1.__dict__)
