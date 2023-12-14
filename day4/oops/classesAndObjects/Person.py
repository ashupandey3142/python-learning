# Python is an object oriented programming language.
#
# Almost everything in Python is an object, with its properties and methods.
#
# A Class is like an object constructor, or a "blueprint" for creating objects.
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    # Add Methods
    def myfunc(self):
        print("Hello my name is " + self.name)

    def printname(self):
        print(self.name)


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
print(p1)
p1.myfunc()

# Modify Object Properties
p1.age = 40
print(p1)

# Delete Objects
# del p1
