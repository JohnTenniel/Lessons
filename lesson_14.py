# досмотреть, и разобраться с использованием символа * и с lambda
# map(func, iterable) , filter(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mult, lst))
# # lst2 = tuple(map(mult, lst))
# lst2 = tuple(map(lambda t: t * 2, lst))
# print(lst2)
#
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# # res = list(map(lambda x, y: (x, y), st, num))
# res = dict(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1,2,3]
# l2 = [4,5,6]
#
# print(list(map(lambda x, y:x+y, l1, l2)))

# t = ('abcd', 'abc', 'abcdi', 'ert', 'def')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [60, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint
#
# n = [randint(1, 40) for i in range(10)]
# print(n)
# print(list(filter(lambda x: x >= 10 and x <= 20, n)))

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
# test = hello
# print(test())

# def my_decorator(func):  # Декорирующая функция
#     def inner():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return inner
#
#
# @my_decorator  # декоратор, работает также как my_decorator(func_test)
# def func_test():  # декорируемая фонкция
#     print("Hello, I am func 'hello'")
#
#
# def hello():  # на эту функцию уже не работает тот деократор, чтобы он заработал
#     # надо перед ней тоже поставить @my_decorator
#     print("Hello, I am func 'hello'")
#
#
# # test = my_decorator(func_test)
# # test()
# func_test()
# # без декоратора (@my_decorator, который ссылает к декорируемой функции)
# # выведется только "Hello, I am func 'hello'"
# hello()
# # Декоратор не влияет на работу функции, а добавляет как бы оформление

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# # @italic
# @bold
# @italic  # Порядок декораторов имеет значение, то что выше то и с краю
# def hello():
#     return "text"
#
#
# print(hello())

# i = 0


# def deco(func):
#     i = 0
#
#     def wrap():
#         nonlocal i
#         i += 1
#         func()
#         # global i
#         # i += 1
#         print("Вызов функции:", + i)
#
#     return wrap
#
#
# @deco
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def warp(arg1, arg2):
#         print("Данные", arg1, arg2)
#         fn(arg1, arg2)
#     return warp
#
# @args_decorator
# def print_full_name(name, surname):
#         print("Меня зовут", name, surname)
#
#
#
# print_full_name("Ирина", "Ветрова")

# def args_decorator(fn):
#     def warp(*args, **kwargs):
#         print("args", *args)
#         print("kwargs", **kwargs)
#         fn(*args, **kwargs)
#
#     return warp
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print("Меня зовут", name, surname)
#
#
# print_full_name("Ирина", "Ветрова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#     return wrap
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")


# def args_dec(fn):
#     def wrap(x, y):
#         print("Сумма:", x, "и", y, "=", end=" ")
#         fn(x, y)
#
#     return wrap
#
#
# @args_dec
# def summa(a, b):
#     print(a + b)
#
#
# summa(5, 2)

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

def multiply(arg):
    def decor(fn):
        def wrap(*args, **kwargs):
            return arg * fn(*args, **kwargs)

        return wrap
    return decor


@multiply(3)
def return_num(num):
    return num


print(return_num(5))