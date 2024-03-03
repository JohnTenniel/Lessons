import random

collw = 0
w, h = 4, 3

matrix = [[(random.randint(-20, 10)) for i in range(h)] for i in range(w)]

for row in matrix:
    for col in row:
        if col < 0:
            collw += 1
            print(col, end="\t")
        else:
            print(col, end="\t")
    print()
print("Количество отрицательных элементов: ", collw)
