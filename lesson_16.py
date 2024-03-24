# print(chr(97))  # вывод символа по коду символа chr

# a = 122
# b = 97
# for x in range(min(a, b), max(a, b) + 1):
#     print(chr(x), end=' ')


from random import randint

min_ascii = 33
max_ascii = 126


def rand_pass():
    res = ''
    for i in range(6):
        res += chr(randint(min_ascii, max_ascii + 1))
    return res




print("Vash parol: ", rand_pass())
