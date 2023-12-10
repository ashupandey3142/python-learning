# A function is a block of code which only runs when it is called.
def greet(name, ending):
    print("Hello, " + name + "!")
    print(ending)


greet("Alice", "Thank you for contacting us !")


def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)
print(result)


# Arbitrary Arguments
# If we don't know how many argument going to pass in function then use * before
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Default Parameter Value
def my_function2(country = "Norway"):
    print("I am from " + country)


my_function2("Sweden")
my_function2()


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print("fibonacci series ....")
for i in range(1,5):
    print(fib(i))


# keyword arguments
def greet2(name, greeting):
    print(f"{greeting}, {name}!")


# Calling the function with keyword arguments
greet2(name="Bob", greeting="Hi")
