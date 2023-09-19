
# Methods

# Method is nothing but a function. If we define a function in side of a class then it will be called as Method

class Students:

    def __init__(self, firstname, lastname, fee):
        self.firstName = firstname
        self.lastName = lastname
        self.fee = fee


    def fullname(self):
        return f'{student1.firstName} {student1.lastName}'

    def tuitionFee(self):
        return f'{self.fullname()} paying {student1.fee}'

student1 = Students("Harsha", "Reddy", 30000)
print(student1.fullname())
# Output is : Harsha Reddy
print(Students.fullname(student1))      # We can write like this also it will also print the same message as line nu 20
print(student1.tuitionFee())
# Output is : Harsha Reddy paying 30000