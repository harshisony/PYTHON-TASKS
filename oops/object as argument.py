class Person:
    pass
#function should be outside the class
def celebrate_birthday(person,name,age):
    person.age=age
    person.name=name
    person.age += 1
    print(f"Happy birthday, {person.name}! You are now {person.age} years old.")

# Creating a Person object
john = Person()

# Passing the Person object as an argument
celebrate_birthday(john,"Harshi",20)

# The age of the original object has been incremented
print(f"{john.name} is now {john.age} years old.")

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def celebrate_birthday(person):
    person.age += 1
    print(f"Happy birthday, {person.name}! You are now {person.age} years old.")

# Creating a Person object
john = Person("John", 30)

# Passing the Person object as an argument
celebrate_birthday(john)

# The age of the original object has been incremented
print(f"{john.name} is now {john.age} years old.")'''
