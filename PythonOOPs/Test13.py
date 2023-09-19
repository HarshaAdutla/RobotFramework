
class Employee:

    def __init__(self,fname, lname, age):
        self.fname = fname
        self.__lname = lname
        self.age = age

    def fullname(self):
        return f'{self.fname} {self.__lname}'

emp = Employee('Harsha', 'Reddy', 25)
print(emp.fname)
print(emp.__lname)      # This will throw an error bcz __lname is a private variable, so we can't print it directly

"""
To print the private variable we need to define a getter method then only we can print the private variable.
"""
