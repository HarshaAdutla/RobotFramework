
# Polymorphism
"""
-> Polymorphism is nothing but responding different types for the same function/method. We can achieve this polymorphism
by using Overriding and Overloading methods.
-> We can override the variables and methods.
"""

"""
When we call child class object it will look for child class variables if it didn't find any then it will look for the 
same on parent class.
"""

# Variable Overriding


class Firstclas:
    name = "Harsha"


class Secondclass(Firstclas):
    # name = "Viswa"
    pass


obj = Secondclass()
print(obj.name)

"""
-> Here in both classes we defined same variable(name) but with different values. And second class is extended from 
first class.
-> In line no 15 I am printing the name of second class (It will print Viswa as output bcz name had Viswa as value in
the second class)
-> Now I have commented the 12th line and calling the same functionality in line no 15 again this time it will print 
Harsha as output. Bcz name is not defined in the second class(#commented) so it will search the same on first class and 
printed the respective value.
-> So the same function is responded in different types.
-> So here we saw the variable overriding.
"""

# Method Overriding

class Big:

    def bigger(self):
        return "This is a 'bigger' method"

class Small(Big):
    # pass
    def bigger(self):
        return "This is a 'smaller' method"
        pass



obj = Small()
print(obj.bigger())


"""
-> Here I have defined same method in both classes and created an object for the small class.
-> And now I am calling a method (bigger i.e defined in both class). So it will look in the Small class and executes the
script.
-> Now I am commenting the bigger method in the Small class now it will look for that in parent class(i.e Big) and 
executes the functionality of that class method.
-> So same functionality responding differently.
-> This is method overriding.

"""