# Variables
# Variable used to store data in python
a = "new word"
print(a)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y, z)

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"

print(f"Hey x value is {x}, y values is {y}, z value is {z}")

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
