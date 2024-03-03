# def get_sum(a, b, c=0, d=1):  # если стоит переменная = значение это на случай если не указаны все переменные в вызове
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 7))
# print(get_sum(1, 5, d=7))
# print(get_sum(1, 5))


# def set_param(c=20, s="-"):
#     print(s*c, end="")
#     print()
#
# set_param()
# set_param(7)
# set_param(20,"#")
# set_param(s="#")

# def get_sum(a):
#     summ = 0
#     if n == 1:
#         for i in str(a):
#             if int(i) % 2 == 0:
#                 summ += int(i)
#
#     elif n == 2:
#         for i in str(a):
#             if int(i) % 2 != 0:
#                 summ += int(i)
#     else:
#         return "Error!"
#     return summ
# n = int(input("вид 1 -чет 2 - нечет:"))
# print()
# print(get_sum(9874023))  # 14 19
# print(get_sum(38271))  # 10 11
# print(get_sum(123456789))  # 20 25

# def get_sum(a, even=True):
#     summ = 0
#     if even:
#         for i in str(a):
#             if int(i) % 2 == 0:
#                 summ += int(i)
#     if not even:
#         for i in str(a):
#             if int(i) % 2 != 0:
#                 summ += int(i)
#     return summ
#
# print()
# print(get_sum(9874023))  # 14 19
# print(get_sum(38271))  # 10 11
# print(get_sum(123456789))  # 20 25
# print()
# print(get_sum(9874023, even=False))  # 14 19
# print(get_sum(38271, even=False))  # 10 11
# print(get_sum(123456789, even=False))  # 20 25

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Eugene", 23)
# print()
# display_info(23, "Eugene")
# print()
# display_info(age=23, name="Eugene")

# print(tuple(2 ** i for i in range(1, 13)))

#
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             temp = tpl.index(el)
#             temp2 = tpl.index(el, temp + 1)
#             return tpl[temp:temp2 + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# распаковка кортежа
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()
# user = get_user()
# print(first_name)
# print(year)
# print(married)
# print(user[0])
# print(user[1])
# print(user[2])
# print(first_name, year, married)

