n = int(input("Количество символов: "))
n1 = input("Тип символов: ")
n2 = int(input("ориентация линии(0 - вертикальная, 1 - горизонтальная): "))

for i in range(n):
    if n2 == 0:
        print(n1, end="\t")
    elif n2 == 1:
        print(n1)
    else:
        print("Такой ориентации линии нет!")
        break
