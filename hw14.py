# вывод чисел будет в float формате, т.к. неизвестно какие цифры могут быть использованы,
# как разделить на int и float пока не смог придумать.
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
def summ():
    n = 0
    print('Вводите цифры, чтобы остановить введите пустую строку:')
    while True:
        args = input('->')
        if not args:
            break
        else:
            try:
                args = float(args)
            except:
                print("only num")
                continue
            n += args
            if args != 0:
                global count
                count += 1

    return n


print(summ())
