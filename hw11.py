def dict_new(*args):
    result = {}
    for arg in args:
        if type(arg) is dict:
            result[str(arg)] = arg
        elif type(arg) is list:
            result[str(arg)] = arg
        else:
            result[arg] = arg
    return result


# не понял нужно ли добавлять ручной ввод, а также должно-ли работать со словарями и списками, поэтому так:
print(dict_new('grey', 1, [27, -72, 'Zombie'], {'a': 5, 'b': 50}, (2, 17)))
print(dict_new(1, 2, 3, 4))
print(dict_new('grey', (2, 17), 3.11, -4))
