

class Employee:

    def __init__(self, fname, mname, lname, age):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.age = age


    @property
    def fullname(self):
        return f'{self.fname} {self.mname} {self.lname}'

    @fullname.setter
    def fullname(self, name):
        fname, lname, mname = name.split(' ')
        self.fname = fname
        self.mname = mname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        print("Name is deleted successfully.")
        self.fname = ""
        self.mname = ""
        self.lname = ""

    @property
    def email(self):
        return f'{self.fname}{self.mname}.{self.lname}@gmail.com'

emp = Employee("Harsha", "Vardhan", 'Reddy',  26)

print(emp.fullname)
print(emp.email)
emp.fname = "Reddy"
print(emp.fullname)
print(emp.email)

emp.fullname = "Viswa mohan Reddy"
print(emp.fullname)
print(emp.email)

"""
In above I have sent a name in string, it will split with spaces and store in the respective attributes.
"""

del emp.fullname
print(emp.fullname)

"""
In above I have deleted the full name so print statement in the fullname deleter method will be executed.
"""

"""
We were able to delete the fullname by using deleter. So here we didn't used any setter and getter methods but we
achieved those functionalities by using property decorator.
"""
