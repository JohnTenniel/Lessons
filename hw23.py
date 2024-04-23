import math


class Geometric:
    count = 0

    @staticmethod
    def triangle_area(a, b, c):
        p = (a + b + c) / 2
        Geometric.count += 1
        return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 1)

    @staticmethod
    def triangle_area_osn(w, h):
        Geometric.count += 1
        return round((1 / 2) * w * h)

    @staticmethod
    def sq_area(a):
        Geometric.count += 1
        return round(a ** 2)

    @staticmethod
    def long_sq_area(a, b):
        Geometric.count += 1
        return round(a * b)

    @staticmethod
    def calc():
        return Geometric.count


print(f"Площадь треугольника по формуле Герона: {Geometric.triangle_area(3, 4, 5)}")
print(f"Площадь треугольника через основание и высоту: {Geometric.triangle_area_osn(6, 7)}")
print(f"Площадь квадрата: {Geometric.sq_area(7)}")
print(f"Площадь квадрата: {Geometric.long_sq_area(2, 6)}")
print(f"Площадь квадрата: {Geometric.calc()}")
