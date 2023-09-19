
"""
Basically when we call any function/method from a class we will use parenthesis but if we define that function/method
by adding @property then we don't need to mention parenthesis.
"""

class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay


    def fullname(self):     # Defining a function
        return f'{self.fname} {self.lname}'

    @property
    def email(self):     # Here I have created this method using property decorator. So I can call this method directly.
        return f'{self.fname}.{self.lname}@gmail.com'

emp = Employee("Harsha", "Vardhan", 4000)
print(emp.fullname())       # Fullname is a method so calling with parenthesis

print(emp.email)   # This is a method, but I am not giving the parenthesis bcz I have defined it with property decorator
emp.fname = "Reddy"

print(emp.fullname())
print(emp.email)