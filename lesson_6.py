import random

# # print(random.random())
# # print(random.randint(1, 9))  # от 1 до 9 - шже 9 включительно (только 2 параметра начало и конец интервала)
# # print(random.randrange(9))  # от 0 до 9 не включая 9
# # print(random.randrange(3, 9))  # от 3 до 9 не включая 9
# # print(random.randrange(3, 9, 2))  # от 3 до 9 не включая 9, 2 - шаг генерируемого значения
# # print(random.uniform(10.5, 25.5)) #вещественные числа
# # print(round(random.uniform(10.5, 25.5)),2) #вещественные число с округлением
#
# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# # random.shuffle(s)  # перемешали элементы в списке
# # print(s)
# print(random.choice(s))  # рандомный элемент из заданной последовательности
# print(random.choices(s))  # рандомный элемент из заданной последовательности в виде списка
# print(random.choices(s, k=3))
# # рандомный элемент из заданной последовательности в виде списка
# # k - кол-во элементов для выборки
#
#
# # import должен быть в самом верху? если что-то есть выше то оно должно быть закоментировани

# list = [random.randint(0, 100) for i in range(10)]  # генератор рандомного списка
# print(list)

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# s = ['20', '30', '40', '50', '60', '70', '80', '90', '10']
# print(s)
# print(len(s))
# # print(sum(s))
# print(min(s))
# print(max(s))

# s = [random.randint(0, 100) for i in range(10)]
# print(s)
# print(max(s))
# mux = max(s)
# s.remove(max(s))
# s.insert(0, mux)
# print(s)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x) # in проверка находится ли в списке или строке или еще где, если not in то
# проверка что нет того что ищещь в списке
# print('e' in x)
# print('1' in x)
#
# l = 'hello'
# print(l)
# print('e' in l)

# n1 = int(input("Введите резмер первого списка: "))
# n2 = int(input("Введите резмер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# c = list()
# d = a
# e = list()
# f = list()
# print('a', a)
# print('b', b)
# c = a + b
# print('c', c)
# for i in a:
#     if a.count(i) > 1:
#         a.remove(i)
# for i in b:
#     if i not in a:
#         d.append(i)
# print('d', d)
# for i in a:
#     if i in b and i not in e:
#         e.append(i)
# print('e', e)
# f.extend((min(a), min(b), max(a), max(b))) # или f = [min(a), min(b), max(a), max(b)]
# print(f)

# n = list(set(random.randint(0, 10) for i in range(10)))
# print(n)

# n1 = 10
# a = []
# while len(a) != n1:
#     n = random.randrange(n1)
#     if n not in a:
#         a.append(n)
# print(a)
# matrix = [[0 for _ in range(3)] for _ in range(3)]
# for i in range(3):
#     for j in range(3):
#         matrix[i][j] = random.randint(0,10)
# print(matrix)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix, end="\n\n")
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col], end="\t")
#     print()
# print()
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()
# print()
# for row in matrix:
#     for col in row:
#         print(col**2, end="\t")
#     print()

# w, h = 5, 3 # в даннос случае h - столбцы w - строки
# matrix = [[random.randint(1, 20) for col in range(h)] for row in range(w)]
# print(matrix)
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()
# print()
# matrix = []
# for row in range(w):
#     new_row = []
#     for col in range(h):
#         new_row.append(random.randint(1, 20))
#     matrix.append(new_row)
# print(matrix)
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()

# w = h = 10
# matrix = [[(1 if col == row or col == (row+1)  or col == (row-1)else 0) for col in range(h)] for row in range(w)]
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)
#     # сколько переменных столько и значений должно быть во вложенных списках, даже если они
#     # не будут использоваться
