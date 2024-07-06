# перегрузка операторов

# число секунд в 1 дне: 86400

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

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.sec < other.sec

    def __le__(self, other):
        return self.sec <= other.sec


c1 = Clock(100)
c2 = Clock(200)
print(c1.get_format_type())
print(c2.get_format_type())
c3 = c1 + c2
print(c3.get_format_type())
# c1 += c2
# print(c1.get_format_type())
c4 = c1 + c2 + c3
print(c4.get_format_type())
c5 = c4 - c2
print(c5.get_format_type())
if c1 == c2:
    print("Время равно")
else:
    print("Время разное")
if c1 != c2:
    print("Время разное")
else:
    print("Время равно")
print(c1.get_format_type() < c2.get_format_type())
print(c1.get_format_type() <= c2.get_format_type())
#Досмотреть

