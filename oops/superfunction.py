#super() = Function used to give access to the methods of a parent class.
#Returns a temporary object of a parent class when used
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling the __init__ method of the parent class
        self.age = age

    def display(self):
        super().display()  # Calling the display method of the parent class
        print("Age:", self.age)

child = Child("Alice", 10)
child.display()

'''class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())'''
