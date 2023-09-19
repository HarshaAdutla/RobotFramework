
class Employee:

    def __init__(self, fname, lname, age):
        self.__fname = fname
        self.__lname = lname
        self.age = age

    def fullname(self):
        return f'{self.__fname} {self.__lname}'

    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname

emp = Employee("Harsha", "Reddy", 25)
print(emp.get_fname())      # Here we are printing the fname by creating a getter method in the class
print(emp.get_lname())      # Here we are printing the lname by creating a getter method in the class

emp.__lname = "Adutla"

print(emp.get_lname())      # lname won't be updated bcz it's a private variable
"""
Once object is created for a class then we can't change the values of private variables. To do that we need to create 
setter method (Like how we did for getter method)
"""