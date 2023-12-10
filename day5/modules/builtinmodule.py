# Built-in Modules
import platform
import datetime
import math
import mymodule

x = platform.system()
print(x)

# dir() Function
x = dir(platform) # There is a built-in function to list all the function names (or variable names) in a module
print(x)

list_all_function = dir(mymodule)
print(list_all_function)


date = datetime.datetime.now()
print(date)
print(date.year)
print(date.month)
print(date.day)
print(date.weekday())

# Creating Date Objects
x = datetime.datetime(2020, 5, 17)
print(x)



# Math Module
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = pow(4, 3)
print(x)

x = math.sqrt(64)
print(x)

x = math.ceil(3.4) # nearest bigger integer
y = math.floor(2.4) # nearest smaller integer

print(x)
print(y)

x = math.pi
print(x)
