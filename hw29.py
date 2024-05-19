class check:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{self.__name} должна быть положительным числом")
        instance.__dict__[self.__name] = value


class Order:
    price = check()
    quantity = check()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_info(self):
        return f"{self.name}: цена {p.price}, количество {p.quantity}, цена за весь товар {p.price * p.quantity}"


p = Order('apple', 5, 10)
print(p.get_info())
