
class Teacher:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def fullname(self):
        return f'{self.fname} {self.lname}'


class Professor(Teacher):

    def __init__(self, fname, lname, pay, technology):
        super().__init__(fname, lname, pay)
        self.technology = technology

tea1 = Teacher('Harsha', 'vardhan', 4000)
print(Teacher.fullname(tea1))

prof1 = Professor('Viswa', 'mohan', 5000, 'python')
print(Professor.fullname(prof1))
print(f'{prof1.fname} knows {prof1.technology}')