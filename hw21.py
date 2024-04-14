class Car:
    def __init__(self, name, year, maker, power, color, price):
        self.name = name
        self.year = year
        self.maker = maker
        self.power = power
        self.color = color
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        if isinstance(year, int):
            self.year = year

    def set_maker(self, maker):
        self.maker = maker

    def set_power(self, power):
        if isinstance(power, int):
            self.power = power

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        if isinstance(price, int):
            self.price = price

    def get_name(self):
        return self.name

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_maker(self):
        return self.maker

    def get_power(self):
        return self.power

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def get_car(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f'Название модели: {a.name}')
        print(f'Год выпуска: {a.year}')
        print(f'Производитель: {a.maker}')
        print(f'Мощность двигателя: {a.power}')
        print(f'Цвет: {a.color}')
        print(f'Цена: {a.price}')
        return 40 * "="


a = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
print(a.get_car())
a.set_name("3")
a.set_year(2017)
a.set_maker("mazda")
a.set_power("450 л.с.")
a.set_color("black")
a.set_price("760000")
print(a.get_car())
