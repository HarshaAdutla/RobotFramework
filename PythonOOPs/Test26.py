
from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def methodOne(self):
        pass

    @abstractmethod
    def methodTwo(self):
        pass

class Child(Parent):

    def __init__(self, name):
        self.name = name

obj = Parent()      # I have tried to create an instance for Parent class
# Output is : Can't instantiate abstract class Parent with abstract methods methodOne, methodTwo
# It is an abstract class now. We can't create instance for abstract classes
obj1 = Child()

"""
-> If we use abstractmethod decorator for one method in a class then the entire class becomes an abstract class.
-> We can't create instance for child class also bcz it is extended from abstracted parent class.
"""