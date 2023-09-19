
class Polygon:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

class Triangle(Polygon):

    def area(self):
        return self.get_width() * self.get_height()

class Rectangle(Polygon):

    def area(self):
        return self.get_width() * self.get_height()

class Namasthe(Triangle, Polygon):

    def __init__(self, area, width, name):
        super().__init__(area, width)
        self.name = name

    def name(self):
        return self.name()



Triangle = Triangle(12, 10)
print(Triangle.area())
Rec = Rectangle(21,12)
print(Rec.area())