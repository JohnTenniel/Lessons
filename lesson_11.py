# функиция zip


# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# # d = dict(a) - будет ошибка при таком обращении списка в словарь
# d = dict(zip(a, b))  # будет создан словарь из списка,
# # используется 2 списка 1 из которых станет ключом второй значением,
# # причем тот который написан первый это ключ а второй значение,
# # т.е. a,b - a ключ b значение  b,a - b ключ a значение
# print(d)
# c = list(zip(b, a))  # получим список из кортежей
# print(c)
# # zip это функция встроенная нужна для объединения нескольких элементов в 1
# # zip может принимать лююбое кол-во элементов, но если превращать в словарь список и прочее
# # то ограничение будет только по кол-ву которое идет для их создания, но должно быть одинаково
# # кол- во элементов в используемых значениях(списках или кортежах) которые мы добавляем в зип.
# # иначе будет выбраны эементы по минимальному кол-ву у одного из используемых элементов

# one = {'name': 'Igor', 'surname': 'Doe', 'job': 'Consultant'}
# two = {'name': 'John', 'surname': 'Ivanov', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# lt = [('Dec', 12), ('Jan', 1), ('Feb', 2)] #распаковка кортежа через зип
# a, b = zip(*lt)  # почитать по символ звездочки
# print(a)
# print(b)

# a = [1, 2, 3]
# # b = [*a, 4, 5, 6] #если есть * убираются [] у а и получается 1 сплошной список [1, 2, 3, 4, 5, 6],
# # вместо[[1, 2, 3], 4, 5, 6] ,
# # и не важно где стоит а если прямо перед ней звездочка [4,*a, 5, 6], тоесть мы как
# # бы распаковываем этот список илтии что-то еещ в тот который вокруг него
# b = [a, 4, 5, 6]
# print(b)
# print(len(b))

# first = {'one': 1, 'two': 2}
# second = {'three': 3, 'four': 4}
# print({**first, **second}) # обьединение двух словарей в 1 с помощью **,
# # тоесть распаковка каждого словаря в общий, но работает только в такой связки,
# # такая запись без ** или без внешниик {} не будет работать
# # ** работает только со словарем, * работает слюбым итерируемым значением
# #почему только в таком порядке работают **:
# # без {}это просто перечисление 'one': 1, 'two': 2 и такого не может быть,
# # без ** это 1 словарь станет ключем а 2 значением что тоже не может быть
# for k, v in {**first, **second}.items():
#     print(k, '->', v)

# first = {'one': 1, 'two': 2}
# second = {'three': 3, 'four': 4}
# a = {**first, **second}
# for k, v in a.items():
#     print(k, '->', v)

# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ')', color, sep="")
#     i += 1
# print()
# for num, val in enumerate(colors):  # enumerate - еще одна встроенная функция для нумерации, по умолчанию с 0
#     print(num, ')', val, sep='')0
# print()
# for num, val in enumerate(colors,3):  #start - тоесть 2 значение в  enumerate это с какого числа начать нумирацию,
#     # само слово start можно не писать
#     print(num, ')', val, sep='')

# studs = {}
# n = int(input('Кол-во студентов: '))
# s = 0
# for i in range(n):
#     name = input(str(i + 1) + '-й студент: ')
#     point = int(input("Балл: "))
#     studs[name] = point
#     # s += point
#
# s = sum(studs.values())
# avg = s / n
# print(studs)
# print('Средний балл: ', avg)
# for i in studs:
#     if studs[i] > avg:
#         print(i)
# или такой вариант вывода:
# for k, v in studs.items():
#     if v > avg:
#         print(k)

# почитать и вспомнить про args и kwargs(или как там второй)
# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7, 'abc'))

# def summa(*params):
#     print(params)
#     print(*params)
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3))
# print(summa(1, 2, 3, 4, 5, 6))

# def ch(*args):
#     avg = sum(args)/len(args)
#     print(avg)
#     res = []
#     for num in args:
#         if num < avg:
#             res.append(num)
#     return res
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def print_scores(student, *scores):
#     print("Student name: ", student, end=", Оценки: ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
# print_scores('Jonatan', 100, 95, 88, 92, 99, 84)
# print_scores('Rick', 96, 20, 33, 66)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Irina", surname="Sharma", age="22")
# intro(name="Igor", surname="Wood", email="sdfsd@sdf.net", country="RF", age="22")

# # def func(a, *args):
# # return a, args
# # def func(a,b,*0args):
# #     return a,b, args
# def func(a,b,c, *args):
#     return a,b,c, args
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8))

# def func(a, b, c, *args, y=0, x=9, **kwargs):
#     return a, b, c, args, kwargs, y, x
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, y=100, n=9, m=10))
# # print(func(1, y=100, 2, 3, 4, 5, 6, 7, 8, n=9,m=10)) # будет ошибка
# # print(func(1, 2, 3, 4, y=100, 5, 6, 7, 8, n=9,m=10)) # будет ошибка

# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# print('my_dict = ', my_dict)
# db(k1=22, k2=31, k3=11, k4=91)
# print('my_dict = ', my_dict)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print('my_dict = ', my_dict)

# name = "Tom"
#
#
# def hi():
#     global name #делает переменную в этой функции глобальной, но только если вызов этой функции
#     # был раньше вызова других, если что то было до этого то в них будет изначальное
#     name = "Sam"
#     # hello Sam Johnson - если добавить новый нэйм то она аменится только локально а
#     # во 2 функции будет использована глобальная переменная
#     # Good bye Tom
#     # Tom
#     surname = "Johnson"
#     print("hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
# print(name)
# bye()
# hi()
# bye()
# print(name)
# # print(surname) #так как эта переменная обьявлена только в фунгкции
# # и она локальная получить за пределами функции к ней доступ нельзя



