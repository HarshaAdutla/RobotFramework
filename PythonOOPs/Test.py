class Animal:
    type = 'pet animal'

    def __init__(self, name):
        self.name = name


# Creating multiple objects with multiple variables for a single class
obj1 = Animal("dog")  # First object
print(f'{obj1.name} is a {Animal.type}')
# Output is : dog is a pet animal

obj2 = Animal("Lion")
print(f'{obj2.name} is not a {Animal.type}')


# Output is : Lion is not a pet animal


class Users:
    species = 'Human'

    def __init__(self, name, age):
        self.name = name
        self.age = age


user1 = Users("Harsha", 26)
user2 = Users("vishwa", 28)

print(f'{user1.name} is a {Users.species} with the age {user1.age}')
# Output is : Harsha is a Human with the age 26

print(f'{user2.name} is a {Users.species} with the age {user2.age}')
# Output is : vishwa is a Human with the age 28
