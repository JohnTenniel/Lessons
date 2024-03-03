# ключами словаря могут быть: число, текст, кортеж и любой неизменяемый тип данных, также булевое то-есть True и False
# список и словарь (list и dict) изменяемый значит он не может быть ключом словаря, а только означением
# словарь не может содержать дубликаты ключей поэтому если есть 2 одинаковых ключа
# то значение будет выведено только то которое было у последнего по счету от начала

# d = {'x1': 3,'x2': 7, 'x3': 5, 'x4': -1}
# temp = 1
#
# for i in d:
#     temp *= d[i]
# print(temp)


## - тут было задание пока я отходил, посомтреть его почти в начале урока

#
# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")
#
# # while True:
# #     n = input("№: ")
# #
# #
# #     if n != '0':
# #         if n in goods:
# #             goods[n][1] = int(input("Количество: "))
# #         else:
# #             print("Такого товара не существует!")
# #     else:
# #         break
# #
# # for i in goods:
# #     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
# for i in goods:
#      print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# for i in d.values():
#     print(i)
#     print()
# for i in d.keys():
#     print(i)
# print()
# for i in d.items():
#     print(i)
# print()
# for i,j in d.items():
#     print(i)
#     print(j)
#     print(i,'->', j)

# чаще всего используют методы апдейт, айтемс, поп и вейлюс

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
#
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print(d)
# d['location'] = d.pop('city')
# print(d)

# досмотреть последний час!!!!