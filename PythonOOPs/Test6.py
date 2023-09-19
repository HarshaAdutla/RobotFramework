
# Inheritance:

class Students:
    def __init__(self, fname, lname, fees):
        self.fname = fname
        self.lname = lname
        self.fees = fees

    def fullname(self):
        return f'{self.fname} {self.lname}'

    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'

class Teacher(Students):
    pass


stu1 = Students('Harsha', 'Reddy', 3000)
print(Students.fullname(stu1))

tea = Teacher('Viswa', 'mohan', 5000)
print(Teacher.fullname(tea))
print(tea.email())
print(tea.fees)