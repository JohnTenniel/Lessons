#Два варианта решения, один закомментированый.
class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, width, height, color):
        # self.__width = width
        self.width = width
        # self.__height = height
        self.height = height
        super().__init__(color)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"Значение {value} должно быть положительным числом")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"Значение {value} должно быть положительным числом")
        else:
            self.__height = value

    def area(self):
        # if not isinstance(self.__width, int) or not isinstance(self.__height,
        #                                                        int) or self.__width < 0 or self.__height < 0:
        #     raise TypeError("Ширина и высота должны быть числом больше нуля")
        # else:
            print(f"Прямоугольник {self.color}, Площадь:", end="")
            return self.__width * self.__height


rect = Rectangle(10, 20, "green")
print(rect.area())

