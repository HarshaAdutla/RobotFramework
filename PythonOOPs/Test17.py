
class Employee:

    def __init__(self, fname, lname, age):
        self.__fname = fname
        self.__lname = lname
        self.age = age

    def set_fname(self, value):
        self.__fname = value

    def get_fname(self):
        return self.__fname

    def set_lname(self, value):
        self.__lname = value

    def get_lname(self):
        return self.__lname

    def fullname(self):
        return f'{self.__fname} {self.__lname}'

class Dev(Employee):

    def __init__(self,fname,lname, age, technology):
        super().__init__(fname, lname, age)
        self.__technology = technology

    def set_technology(self, value):
        self.__technology = value

    def get_technology(self):
        return self.__technology

emp1 = Employee('Harsha', 'reddy', 25)
emp2 = Dev('viswa', 'mohan',26, 'python')
print(emp1.fullname())
print(emp2.get_technology())
emp2.set_technology("Java")
print(emp2.get_technology())
print(emp2.fullname())