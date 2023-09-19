

class Students:
    fee_hike = 5.5

    def __init__(self, firstname, middlename, lastname, fees):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.fees = fees
        self.email = f'{firstname}{middlename}.{lastname}@gmail.com'


    def fullname(self):
        return f'{self.firstname}{self.middlename} {self.lastname}'


    def apply_fee_raise(self):
        print(self.fees)
        print(self.fee_hike)
        self.fees = float(self.fees) * float(self.fee_hike)

    @classmethod
    def set_raise_percentage(cls, amount):
        cls.fee_hike = amount

    @classmethod
    def from_string(cls, stu_str):
        firstname, middlename, lastname, fees = stu_str.split('-')
        return cls(firstname, middlename, lastname, fees)

stu1 = 'Harsha-vardhan-Reddy-3000'

new_stu1 = Students.from_string(stu1)

print(new_stu1.fullname())
Students.set_raise_percentage(7.0)
print(new_stu1.fees)
new_stu1.apply_fee_raise()
print(new_stu1.fees)
