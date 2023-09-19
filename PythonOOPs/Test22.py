
# Dunder/Magic/Special Methods

"""
Any method that starts and ends with double underscore are called dunder/magic/special methods. We have already seen
__init__ method while initiating the class.
-> Similarly we have so many dunder methods Ex: __repr__ and __str__ .
"""


class Employee:
    raise_amount = 2

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f'{self.fname}.{self.lname}@gmail.com'

    def fullname(self):
        return f'{self.fname} {self.lname}'
    def pay(self):
        return self.pay * self.raise_amount

    def __repr__(self):
        return f'{self.fname},{self.lname},{self.pay}'

    def __str__(self):
        return f'{self.fullname()}, {self.email}, {self.pay}'


obj = Employee("Hasrsha", "vardhan", 3000)
print(obj.fullname())
print(obj.__repr__())
print(obj.__str__())
print(str(obj))