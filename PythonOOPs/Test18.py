
class Car:

    def __init__(self, color, speed):
        self.__speed = speed
        self.color = color

    def public_method(self):
        print(self.__speed)
        print(self.color)

car1 = Car('Green', 150)
car1.public_method()   # Here speed is a private variable we are calling it using method
print(car1.color)      # Here color is a public variable, so calling it directly
