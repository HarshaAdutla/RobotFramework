
class Employee:

    def __init__(self,fname, lname, pay):
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

    def __init__(self,fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def total_emp(self):
        for emp in self.employees:
            print(emp.fullname())


emp1 = Employee('Harsha', 'Reddy', 3000)
dev1 = Dev('viswa', 'mohan', 4000, 'python')
mang1 = Manager('Viswa', 'Reddy', 6000, [emp1])

# mang1.total_emp()
print(mang1.fullname())
print(mang1.pay)
mang1.add_emp(dev1)
mang1.total_emp()
mang1.remove_emp(dev1)
mang1.total_emp()


