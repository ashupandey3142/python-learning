# In Python, functions are first class objects which means that functions in Python can be passed as arguments.
# Properties of first class functions:
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists.

# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))

# we have assigned the function shout to a variable.
# This will not call the function instead it takes the function object referenced by a shout and creates a second name pointing to it, yell

# Example 2: Passing the function as an argument


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)


greet(shout)
greet(whisper)


# Example 3: Returning functions from another function.

def create_adder(x):
    def adder(y):
        return x+y

    return adder


add_15 = create_adder(15)

print(add_15(10))

