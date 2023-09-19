
class Teachers:
    raise_amount = 1.2

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def fullname(self):
        return f'{self.fname} {self.lname}'

    def apply_raise(self):
        self.pay = float(self.pay) * float(self.raise_amount)


class Hod(Teachers):
    raise_amount = 5.2


teacher1 = Teachers('Harsha', 'vardhan', 4000)
hod1 = Hod('Viswa', 'mohan', 10000)

print(Teachers.fullname(teacher1))
print(teacher1.pay)
teacher1.apply_raise()
print(teacher1.pay)

print(Hod.fullname(hod1))
print(hod1.pay)
hod1.apply_raise()
print(hod1.pay)
