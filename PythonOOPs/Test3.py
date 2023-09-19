
class Students:
    fee_hike = 5.5

    def __init__(self, firstname, middlename, lastname, fees):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.fees = fees
        self.email = f'{firstname}{middlename}.{lastname}@gamil.com'



    def fullname(self):
        return f'{self.firstname}{self.middlename} {self.lastname}'


    def apply_fee_raise(self):
        self.fees = float(self.fees * self.fee_hike)

    @classmethod
    def set_raise_percentage(cls, amount):
        cls.fee_hike = amount

student1 = Students("Harsha", "vardhan", "Reddy", 20000)

print(student1.fullname())
print(student1.email)
print(student1.fees)
Students.apply_fee_raise(student1)
print(student1.fees)
Students.set_raise_percentage(6.5)
print(Students.fee_hike)


# Here I have multiple students

student2 = 'Harsha-vardhan-reddy-3000'
student3 = 'Viswa-mohan-Reddy-4000'
student4 = 'Siva-sudheer-Reddy-5000'

firstname, middlename, lastname, fees = student2.split('-')
firstname, middlename, lastname, fees = student3.split('-')
firstname, middlename, lastname, fees = student3.split('-')

stu1 = Students(firstname, middlename, lastname, fees)
student_email = stu1.email
print(student_email)
