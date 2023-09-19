
# Abstraction / Data abstraction

"""
To achieve this abstraction we need to import abstract packages from ABC. That will see in the next script
"""

"""
Abstraction is used to hide all the internal details nd show only the functionality of methods and classes.
"""

# Here I am creating two classes

class One:

    def small(self):
        pass
    def big(self):
        pass

class Two(One):

    def __init__(self, name):
        self.name = name

"""
-> Buy using abstraction we can restrict others to create instance for my classes(Parent).
-> Here class Two is inherited from class One and now I can create instance for parent class(class One) - General flow.
-> To restrict others to not to create instance to my class i will define it as abstract class.(will see it int he next
script).
"""
obj = One()     # Able to create instance for parent class.

"""
-> If I am dev1 and i don't want others to create instance to my class then I will make it as Abstract class so they 
can't create any instance to my class.
-> If they want to use my class methods they have to define them again in their classes only.
"""