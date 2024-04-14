import os

dir_name = input("Полный путь к папке: ")
objs = os.listdir(dir_name)
for obj in objs:
    p = os.path.join(dir_name, obj)
    if os.path.isfile(p):
        print(f'{obj} - file - {os.path.getsize(p)}')
    elif os.path.isdir(p):
        print(f'{obj} - dir')
