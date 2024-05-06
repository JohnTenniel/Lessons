class Clock:
    __Day = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__Day

    def get_format_type(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return x if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    # def __truediv__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом Clock")
    #     return Clock(self.sec / other.sec)
    # Не сработает так как не даст целого числа

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec == other.sec

    def __ne__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec < other.sec

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec <= other.sec

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec >= other.sec


c1 = Clock(600)
c2 = Clock(200)

print("Первое время: " + c1.get_format_type())
print("Второе время: " + c2.get_format_type())
c3 = c1 + c2
print("__add__ : " + c3.get_format_type())
c4 = c1 - c2
print("__sub__: " + c4.get_format_type())
c5 = c1 * c2
print("__mul__ : " + c5.get_format_type())
# c6 = c1 / c2
# print("__truediv__ : " + c6.get_format_type())
# c1 /= c2
# print(c1.get_format_type())
c7 = c1 // c2
print("__floordiv__ : " + c7.get_format_type())
c8 = c1 % c2
print("__mod__ : " + c8.get_format_type())

# c1 += c2
# print(c1.get_format_type())
c1 -= c2
print("c1 -= c2: " + c1.get_format_type())
c1 *= c2
print("c1 *= c2: " + c1.get_format_type())
c1 //= c2
print("c1 //= c2: " + c1.get_format_type())
c1 %= c2
print("c1 %= c2: " + c1.get_format_type())

if c1 == c2:
    print("__eq__: Время равно")
else:
    print("__eq__: Время разное")
if c1 != c2:
    print("__ne__: Время разное")
else:
    print("__ne__: Время равно")
print("__lt__ : ", end="")
print(c1.get_format_type() < c2.get_format_type())
print("__le__ : ", end="")
print(c1.get_format_type() <= c2.get_format_type())
print("__gt__ : ", end="")
print(c1.get_format_type() > c2.get_format_type())
print("__ge__ : ", end="")
print(c1.get_format_type() >= c2.get_format_type())
