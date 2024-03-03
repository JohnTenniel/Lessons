# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# # это кортеж из двух элементов
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("Страна - >", country_name, "\nНаселение - >", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("Город - >", city_name, "\nНаселение города ->",city_population)
#     print()

# множества {set}, кортеж в круглых скобках, список квадратные, множество фигурные.
# множество это неупорядоченная коллекция, каждый перезапуск меняет порядок следования внутри нее,
# это значит что в множество нельзя обратиться по индексу, т.к. оно не упорядочено.
# множестов состоит только из неповторяемых значений, т.е. если юудет s = {"red", "gren", "blue", "red", "gren"} то \
# выведется только {'blue', 'gren', 'red'}, т.е. только уникальные значения и даже len(s) выдаст только 3
# множество это изменяемый тип данных.


# s = {"red", "gren", "blue", "red", "gren"}
# print(type(s))
# print(s)
# print(len(s))
#
# for i in s:
#     print(i)

# a = set("Hello")
# print(a)

# s = [x for x in range(10)]
# print(s)
# s = {x for x in range(10)} #цифры 1-9 будут идти в правильном порядке
# print(s)
# s = {x*x for x in range(10)} # в таком варианте порядок будет другой, но всегда одинаковый
# print(s)
# s = {input("->") for i in range(3)}
# print(s)
# print(s)


# from random import randint
#
# s = {randint(20, 50) for i in range(10)}
# print(s)
# print(len(s))
# #в такой ситуации есть будут случайные одинаковые значения то будет выведено не 10 а столько сктолько разных
# # даже при рандже 10

# s = {"red", "green", "blue"}
# print("green" in s) #проверка существует ли элемент в множестве
# print("green1" in s) #проверка существует ли элемент в множестве
# print("green1" not in s) #проверка существует ли элемент в множестве
# print("green" not in s) #проверка существует ли элемент в множестве

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # lt = [i for i in lst if "a" in i] # Справа от фор в 1 строку может быть только иф но не элс,
# # но элс можно # поставить слева
# # lt = ["A"+i[1:] if i[0] == "a" else "B"+i[1:] for i in lst]
# lt = ["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"]
# print(lt)
# # Расписано как работает сжатый вид, т.е. сначало правая часть потом левая но все это в центральном цикле
# # for i in lst:
# #     if i[1] == 'c':
# #         if i[0] == 'a':
# #             print("A" + i[1:])
# #         else:
# #             print("B" + i[1:])

# s = {"red", "green", "blue"}
# print(s)
# s.add("black")  # добавление в множество
# print(s)
# s.remove("black") #удаление из множества конкретного элемента,
# print(s)

# s.remove("pink") #но если нет такого элемента то будет ошибка Keyerror
# print(s)
# но
# color = "pink"
# if color in s:
#     s.remove("pink")
# print(s)

# s.discard("green")
# print(s)
# s.discard("pink")# тоже удаление только если такого элемента не существует то будет без изменений и без ошибки
# print(s)

# s.pop()  # удаляет 1 элемент множества но случайно, выбрать нельзя в отличает от списков
# print(s)

# s.clear()#полностью очищает множество делая его пустым
# print(s)

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# x = {7, 8}
# y = {9, 8}
#
#
# def poisk():
#     temp = a.union(b, c, d, e, x, y)
#     return temp
#
#
# print(poisk())
# print(len(poisk()))
# print(min(poisk()))
# print(max(poisk()))


# n = "hello"
# m = "how are you"
#
# n = set(n)
# m = set(m)
#
# # n.intersection_update(m)
# a = n.intersection(m)# или n & m
# for i in a:
#     print(i, end=" ")

#
# n = {"Марина", "Женя", "Света"}
# m = {"Костя", "Женя", "Илья"}
#
# a = n.symmetric_difference(m)
# print(a)
# b = n.intersection(m)
# print(b)
# print(n.difference(b))

# можно: s= [] -> s = set(s) -> s = list(s) - перевод из списка в мноество и назад.
# но при возврате назад в лист будут осталены тольк оуникальные элементы
# если переводить из кортежа то будет также тольк оуникальные
# Существует frozenset() - это тоже множество только в отличае от обычного оно не изменяемое

# Словари - dict

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
#
# print(lst)
# print(d)
#
# lst[1] = 200
# d["two"] = 200
#
# print(lst)
# print(d)
#
# print(lst[1])  # для списка обращение по индексу
# print(d["two"])  # для словаря нет индекса но есть обращение по ключу(ключ сдева значение справа через :)

# создание словаря
# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# d1 = dict(one=1, two=2)
# print(d1)
# d2 = dict([["a", 1], ["b", 2]])
# print(d2)
# d3 = dict([("a", 1), ["b", 2]])
# print(d3)
# d4 = dict([("a", 1), ("b", 2)])
# print(d4)
# d4 = dict([{"a", 1}, {"b", 2}]) # числа тоже могут быть ключами
# print(d4)
