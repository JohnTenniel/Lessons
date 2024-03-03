import math

n = int(input("Выберите фигуру:\n 1 - треугольник\n 2 - прямоугольник\n 3 - круг\n"))


def triangle(a, b, c):
    p = (a + b + c) / 2
    return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)


def rectangle(a, b):
    return round(a * b, 2)


def circle(a):
    return round(math.pi * a ** 2, 2)


if n == 1:
    a1 = float(input("Введите первую сторону: "))
    b1 = float(input("Введите вторую сторону: "))
    c1 = float(input("Введите третью сторону: "))
    print(triangle(a1, b1, c1))
elif n == 2:
    a1 = float(input("Введите первую сторону: "))
    b1 = float(input("Введите вторую сторону: "))
    print(rectangle(a1, b1))
elif n == 3:
    a1 = float(input("Введите радиус окружности: "))
    print(circle(a1))
else:
    print("Такой фигуры нет!")