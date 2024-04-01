# import re
# # f = open(r"C:\Users\JohnT\PycharmProjects\PY_TOP_lesson\test.txt", mode='r') # полный путь для доступа к любому файлу
# f = open("test.txt", mode='r') # для r можно либо ничео не ставить либо mode='r' либо просто 'r'
# print(f)
# print(*f)
# print(f.closed)#проверка открыт или закрыт файл
# print(f.mode)#мод редактирования, чтeния или прочее
# print(f.name)#путь к файлу
# print(f.encoding)#кодировка
# f.close() #закрытие текстового файла
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open("test.txt", 'r')
#
# # print(f.read())  # полностью считает то что есть в файле
# print(f.read(3))  # цифра означает сколько символов из файла возьмется, если повто
# print(f.read())  # если повторно прописать рид, то будет дочитан файл до конца
# # рид после close() нельзя ставить будет ошибка потому что файл уже закрыт
# # если с начала сделать полный рид, а потом с цифрами ничего не изменится потому что файл будет прочитан полностью
#
#
# f.close()

# f = open("test1.txt", 'r')
# print(f.readline())
# # print(f.readline(11)) #также как и рид ридлайн дочитывает символы если вывелось не все
# ## и тольк оследующий ридлайн выведет следующую строку
# # print(f.readline())
#
# print(f.readline(15))
# print(f.readline(40))
# print(f.readline(40))
# #если больше ридлайнов чем строчек то ничего не выведет на те команды которые больше чем колличество и не будет ошибки
# # каждая команда открывает одну строку, цифры значат считываемые символы в строке,
# # если символов указано больше чем в строке ко выведет всю
# f.close()


# f = open("test1.txt", 'r')
# # print(f.readlines())#выведет все содержимое файла и вместо переносов и прочего будут спецсимволы которые их создают
# # # \n - перенос строки, и будет список из того что есть в файле
# print(f.readlines(15))  # если хотя-бы 1 буква из строки входит в диапазон она выведется вся,
# # на 14 будет 1 строка на 15 уже 2
# # дочитывание работает также, как и у рид
# f.close()

# f = open("test1.txt", 'r')
# for line in f:
#     print(line)
# f.close()

# count = 0
# f = open("test1.txt", 'r')
# for line in f:
#     count += 1
# print(count)
# f.close()
# # подсчет строк в документе через цикл

# f = open("test1.txt", 'r')
# print(len(f.readlines()))
# f.close()
# # подсчет строк в документе без цикла


# f = open("xyz.txt", 'w')  # если файла нет, то он создастся, если он есть он будет очищен
# f.write("Hello\nWorld")
# f.close()
#
# f = open("xyz.txt", 'r')
# print(f.read())
# f.close()


# f = open("xyz.txt", 'a')#дозапишет то что задано в файл, если файла нет то тоже созхдаст его как и w
# f.write("\nNew text")
# f.close()

# f = open("xyz1.txt", 'a')#дозапишет то что задано в файл, если файла нет то тоже созхдаст его как и w
# f.write("\nNew text")
# f.close()

# f = open("xyz2.txt", 'w')
# f.writelines(['This is line 1','This is line 2','This is line 3']) #если нет \n то запишет все в 1 строку This is line 1This is line 2This is line 3
# f.close()

# lst = [str(i) for i in range(1, 20)]
# print(lst)
# # str(i) потому что write может записывать в документ только текст
# f = open("xyz3.txt", 'w')
# for index in lst:
#     f.write(index + "\t")# если сделать на str(i) а str(index)
#     # то будет не несколько  1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19
#     # а одно число 12345678910111213141516171819
# f.close()

# f = open("xyz3.txt", 'r')
# d = f.read()
# print(d)
# print(type(d))
# f.close()

# lst = [i for i in range(1, 20)]
# print(lst)
#
# # f = open("xyz4.txt", 'w')
# # for index in lst:
# #     f.write("\t".join(str(index)))# 1234567891	01	11	21	31	41	51	61	71	81	9
# # f.close()
#
# f = open("xyz4.txt", 'w')
# f.write("\t".join(map(str, lst)))# 1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19
# f.close()
#
# f = open("xyz4.txt", 'r')
# d = f.read()
# print(d)
# print(type(d))
# n = list(map(int, d.split("\t")))
# f.close()
# print(n)

# file = "text2.txt"
# f = open(file, 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open(file, 'r')
# d = list(f.readlines())
# f.close()
#
# print(d)
# d[1] = "Hello world;\n"
# print(d)
#
# f = open(file, 'w')
# f.write(str("".join(map(str, d))))
# f.close()


# file = "text2.txt"
# f = open(file, 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open(file, 'r')
# d = list(f.readlines())
# f.close()
# print(d)
# i = int(input("pos = "))
# if 0 <= i <= len(d):
#     del d[i]
# else:
#     print("Неверный индекс")
# print(d)
#
# file = "text2.txt"
# f = open(file, 'w')
# f.writelines(d)
# f.close()


# f = open("test.txt")
# print(f.read(3))
# print(f.tell())#показывает позицию на которой находится курсор
# print(f.seek(1))#перемещение курсора в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()
#
# f = open("test.txt", "r+")#можно и прочитать и отредактировать добавив + к любому r,w,a но r+ не затирает файл как w+
# f.write("i am learning Python!")
# print(f.seek(3))
# f.write(" - new string - ")
# print(f.read())
# f.close()
# #i a - new string - n! - , было 2 перезаписи файла первая с hello! на i am learning Python!
# и вторая с i am learning Python! заменило - new string - с 3 символа
# a+ игнорирует движение курсора и всеравно жобавит в конец строки тоесть i am learning Python! - new string -
# a+ и w+ - тоже не могут считать данные как a и w .read(), только r+

# f = open("xyz.txt", 'w')
#
# f.close()

#
# with open('test.txt','w') as f:
#     print(f.write('0123456789'))
#     print(f.closed)
# print(f.closed)

# with open('test.txt', "r") as f:
#     for line in f:
#         print(line[:2])
# #сам файл:
# # 012
# # 34567
# # 89

# encoding="utf-8 - чтобы в run были русские буквы
# def longest_worlds(file):
#     with open(file, 'r', encoding="utf-8") as text:
#         w = text.read().split()
#         print(w)
#         # max_length = max(w, key=len) #поиск самого длинного слова по длинее слов
#         max_length = len(max(w, key=len))  # выводит длинну самого длинного слова
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]  # если слово одно то будет слово если несколько то список
#         return res
#
#
# print(longest_worlds('test.txt'))

# one = 'one.txt'
# two = 'two.txt'

# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
#
# with open(one, 'w') as f:
#     f.write(text)

# with open(one, "r") as fr, open(two, "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

one = 'one.txt'
two = 'two.txt'
three = 'three.txt'

with open(one, "r") as fo, open(two, "r") as ft, open(three, "w") as fw:
    # a = fo.read() + ft.read()
    # print(a)
    fw.write(fo.read() + "\n" + ft.read())
# если использовать readlines, то тогда и writelines
