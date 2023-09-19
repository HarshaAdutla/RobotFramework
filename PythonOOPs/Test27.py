from abc import ABC, abstractmethod


class One(ABC):

    @abstractmethod
    def methodOne(self):
        print("Parent clas first method")

    @abstractmethod
    def methodTwo(self):
        print("Parent class second method")

class Two(One):

    def __init__(self, name):
        self.name = name

    def methodOne(self):
        print("Child class firs method" + self.name)

    def methodTwo(self):
        print("Child class second method")

obj = Two("Harsha")
"""
-> Here I have created parent class abstract methods in the child class, so now I am able to create an instance for the 
child class even though it is extended from abstracted parent class.
-> If we didn't create abstracted methods in the child class we can't create instance for child class also, but if we
define those methods in the child class then we can able to create instance for the child classes.
-> Here class Two is extended from parent class(One which is an abstracted class) but I am able to create an instance
bcz I have created those methods(Which are abstracted in parent class) in the child class. So now I can create instance
for child class even though it is extended from abstracted class.
"""