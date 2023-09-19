
# Private Methods

class Car:

    def __init__(self, color, speed):
        self.__speed = speed
        self.color = color

    def public_method(self):
        print(self.__speed)
        print("It is a public method")
        self.__private_method()


    def __private_method(self):
        print("It is a private method")

car1 = Car('Red', 250)
car1.public_method()

"""
-> We can't call a private method direclt we must call it inside of a public method.
-> Here I am calling the private method in side the public method. So when public method is called then private method 
will also executes.
"""