
# Overloading a method

"""
-> In previous script we saw how to override the variables and methods, now will see how to overload the methods.
-> In overloading we can't overload variables we can only overload methods.
"""

"""
-> Here I have created a method in way that there re multiple ways to call it.
-> When we call it differently it acts differently, this is known as overloading a method.
"""

class Salary:
    amount = 1000
    raise_amount = 2

    def salaryRaise(self, role, amountToRaise = None):
        self.role = role
        self.amountToRaise = amountToRaise

        if self.role == "Principal":
            if amountToRaise != None:
                salary = self.amount * self.amountToRaise
                print(f'Total amount after raise for {self.role} role is : {salary}')
            else:
                salary = self.amount * self.raise_amount
                print(f'For {self.role}s we are giving basic raise only. '
                      f'So {self.role} will get final amount of: {salary}')


        elif self.role == "HOD":
            salary = self.amount * self.raise_amount + 200
            print(f'Total amount after raise for {self.role} role is : {salary}')

        elif self.role == "Senior_Prof":
            salary = self.amount * self.raise_amount + 500
            print(f'Total amount after raise for {self.role} role is : {salary}')
        else:
            print(f'{self.role} role is not eligible for a raise.')

obj = Salary()
obj.salaryRaise("HOD")
# Output is : Total amount after raise for HOD role is : 2200

obj.salaryRaise("Teacher")
# Output is : Teacher role is not eligible for a raise.

obj.salaryRaise("Senior_Prof")
# Output is : Total amount after raise for Senior_Prof role is : 2500

obj.salaryRaise("Principal", 4)     # Raise defined manually while calling the function
# Output is : Total amount after raise for Principal role is : 4000

obj.salaryRaise("Principal")        # Raise is not defined here
# Output is :  For Principals we are giving basic raise only. So Principal will get final amount of: 2000

"""
-> In above example I have defined only one method with if else blocks, So based on the inputs the same method will 
execute differently.
-> When I pass a role it behaves differently and if I didn't send the value it behaves differently.
-> In line no 46 I have passed role as Teacher, but in the function/method this role doesn't have any raise so it
behaves differently.
"""

"""
-> In above I have defined the raise_amount for all roles and added money like 200 and 500 for different role, but for
Principal role I want to give more hike, So i am passing hike amount while calling the method.
-> So I have defined the amountToRaise as None at the beginning. So that if I didn't define any hikes while calling it 
won't fail the script.
-> I want to give hike to Principal on as my wish so passing the hike amount while calling the method.
"""

