import random


def tup():
    a = tuple(random.randint(0, 5) for i in range(10))
    b = tuple(random.randint(-5, 0) for i in range(10))
    # не до конца понятно, в b включительно 0 или нет, сделал включительно
    return a, b


a, b = tup()
fin = a + b
count = fin.count(0)
print(a)
print(b)
print(fin)
print("0 = ", count)
