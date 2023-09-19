
# Encapsulation

class Employee:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = fname

    def fullname(self):
        return f'{self.fname} {self.lname}'

emp = Employee('Harsha', 'Reddy', 25)
print(emp.age)
print(emp.fullname())
emp.fname = "vardhan"
print(emp.fname)
print(emp.fullname())

# Here we are able to update any attribute. No security to any variable.