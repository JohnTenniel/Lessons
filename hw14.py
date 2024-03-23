count = 0


def arg_deco(func):
    def warp():
        result = func()
        sr = result / count
        print('Сумма чисел:', result)
        print('Среднее арифметическое: ', end="")
        return sr
    return warp


@arg_deco
def summ(*args):
    n = 0
    print('Вводите цифры пока не введете 0:')
    while args != 0:
        args = int(input('->'))
        n += args
        if args != 0:
            global count
            count += 1

    return n


print(summ())
