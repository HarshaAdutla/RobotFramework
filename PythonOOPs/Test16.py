

class Employee:

    def __init__(self, fname, lname, age):
        self.__fname = fname
        self.__lname = lname
        self.age = age

    def fullname(self):
        return f'{self.__fname} {self.__lname}'

    def set_fname(self, value):
        self.__fname = value

    def get_fname(self):
        return self.__fname

    def set_lname(self, value):
        self.__lname = value

    def get_lname(self):
        return self.__lname

    def get_email(self):
        return f'{self.__fname}.{self.__lname}@gmail.com'

emp = Employee("harsha", 'reddy', 25)
print(emp.fullname())
print(emp.get_email())
emp.set_fname("viswa")
emp.set_lname("mohan")
print(emp.age)      #It is not a private variable
print(emp.get_email())
print(emp.fullname())