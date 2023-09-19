
class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def fullname(self):
        return f'{self.fname} {self.lname}'


class Dev(Employee):

    def __init__(self, fname, lname, pay, technology):
        super().__init__(fname, lname, pay)
        self.technology = technology


class Manager(Employee):

    def __init__(self, fname, lname, pay):
        super().__init__(fname, lname, pay)



emp1 = Employee('Harsha', 'vardhan', 4000)
dev1 = Dev('Viswa', 'mohan', 9000, 'python')
mang1 = Manager('Siva', 'sudheer', 8000)

print(isinstance(mang1, Employee))
print(isinstance(dev1, Manager))
print(isinstance(emp1, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Dev))
