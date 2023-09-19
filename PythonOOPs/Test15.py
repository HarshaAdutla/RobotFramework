
class Employee:

    def __init__(self, fname, lname, age):
        self.__fname = fname
        self.__lname = lname


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

emp = Employee('Viswa', 'Mohan', 26)

print(emp.get_fname())
print(emp.get_lname())
print(emp.fullname())
emp.set_fname("Harshavardhan")
emp.set_lname("Reddy Adutla")
print(emp.get_fname())
print(emp.get_lname())
print(emp.fullname())
